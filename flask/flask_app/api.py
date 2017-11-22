#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    : api.py
# @Software: flask_app
# @Function:

from flask import jsonify,abort,request
from flask_app import _api,_client,_pool
from flask_restful import Resource
from flask_app.tasks import files,web,mega_task
import gridfs
import redis
import json


_r = redis.Redis(connection_pool=_pool)



def prefix_url(json):
    if type(json) is list:
        for item in json:
            prefix_url(item)
    if type(json) is dict:
        for items in json.items():
            if 'url' in items:
                items = list(items)
                items[1] = "base_url_/" + items[1]
                lst = list()
                lst.append(items)
                items = dict(lst)
                json.update(items)
            else:
                prefix_url(items[1])

def GFS_Decorator(func):
    def wrapper(self,db_name,file_name):
        __db = _client[db_name]
        self._fs = gridfs.GridFS(__db)
        self._bucket = gridfs.GridFSBucket(__db)
        return func(self,db_name,file_name)
    return wrapper


class Base(object):
    _fs = gridfs.GridFS(_client.get_database())
    _bucket = gridfs.GridFSBucket(_client.get_database())

class ListFile(Resource,Base):
    def get(self,db_name,file_name):
        ret = web.list_file.delay(db_name,file_name)
        return {'name':ret.get()}

class GetFileData(Resource,Base):
    def get(self,db_name,file_name):
        ret = files.get_file_data.delay(db_name,file_name)
        return jsonify(ret.get())

class DeleteFile(Resource,Base):
    def get(self,db_name,file_name):
        ret = files.delete_file.delay(db_name,file_name)
        return jsonify(ret.get())

class PutFile(Resource,Base):
    def post(self,db_name,file_name):
        print(request.form,request.json,request.data)
        if request.form:
            file = request.form.getlist('json_data')[0]
            file = eval(file)
        elif request.json:
            file = request.get_json()
        ret = files.put_file.delay(db_name,file)
        return jsonify(ret.get())
        # json_data = request.get_json()
        # if file_name not in json_data.keys():
        #     return jsonify({'error_no':'02'})
        # data = json_data[file_name]
        # if _r.hset(json_data['quest_name'],file_name,data):
        #     _r.lpush('quest_list',json_data['quest_name'])
        #     _r.lpush(json_data['quest_name'],file_name)
        #     return jsonify({'error_no':'00'})
        # else:
        #     return jsonify({'error_no':'03'})


class TestAPI(Resource):
    def get(self,filename):
        pass

_api.add_resource(ListFile,'/gfsList/<string:db_name>/<string:file_name>')
_api.add_resource(GetFileData,'/gfsGet/<string:db_name>/<string:file_name>')
_api.add_resource(DeleteFile,'/gfsDel/<string:db_name>/<string:file_name>')
_api.add_resource(PutFile,'/gfsPut/<string:db_name>/<string:file_name>')
_api.add_resource(TestAPI,'/gfsTestAPI/<string:db_name>/<string:file_name>')
