#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/23
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
    def wrapper(self,col_name,file_name):
        __db = _client[col_name]
        self._fs = gridfs.GridFS(__db)
        self._bucket = gridfs.GridFSBucket(__db)
        return func(self,col_name,file_name)
    return wrapper


class Base(object):
    _fs = gridfs.GridFS(_client.get_database())
    _bucket = gridfs.GridFSBucket(_client.get_database())

class ListFile(Resource,Base):
    def get(self,col_name,file_name):
        ret = web.list_file.delay(col_name,file_name)
        return {'name':ret.get()}

class GetFileData(Resource,Base):
    def get(self,col_name,file_name):
        ret = files.get_file_data.delay(col_name,file_name)
        return jsonify(ret.get())

class DeleteFile(Resource,Base):
    def get(self,col_name,file_name):
        ret = files.delete_file.delay(col_name,file_name)
        return jsonify(ret.get())

class PutFile(Resource,Base):
    def post(self,col_name,file_name):
        print(request.form,request.json,request.data)
        if request.form:
            file = request.form.getlist('json_data')[0]
            file = eval(file)
        elif request.json:
            file = request.get_json()
        ret = files.put_file.delay(col_name,file)
        return jsonify(ret.get())


_api.add_resource(ListFile,'/gfsList/<string:col_name>/<string:file_name>')
_api.add_resource(GetFileData,'/gfsGet/<string:col_name>/<string:file_name>')
_api.add_resource(DeleteFile,'/gfsDel/<string:col_name>/<string:file_name>')
_api.add_resource(PutFile,'/gfsPut/<string:col_name>/<string:file_name>')
