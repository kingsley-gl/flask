#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

from flask import jsonify,abort,request
from flask_app import _api,_fs,_pool
from flask_restful import Resource
from .task import test
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

class FindFile(Resource):
    def get(self,filename):
        file = _fs.find_one({'filename':filename})
        if file is None:
            abort(404)
        data = json.loads(file.read().decode('utf-8'))
        return jsonify(data)

class DeleteFile(Resource):
    def get(self,filename):
        return jsonify({'aaa':3666})

class PutFile(Resource):
    def post(self,filename):
        json_data = request.get_json()
        if filename not in json_data.keys():
            return jsonify({'error_no':'02'})
        data = json_data[filename]
        if _r.hset(json_data['quest_name'],filename,data):
            #logger.debug('quest_list',json_data['quest_name'])
            #logger.debug(json_data['quest_name'],filename)
            _r.lpush('quest_list',json_data['quest_name'])
            _r.lpush(json_data['quest_name'],filename)
            return jsonify({'error_no':'00'})
        else:
            return jsonify({'error_no':'03'})


class TestAPI(Resource):
    def get(self,filename):
        pass

_api.add_resource(FindFile,'/gfsFind/<string:filename>')
_api.add_resource(DeleteFile,'/gfsDel/<string:filename>')
_api.add_resource(PutFile,'/gfsPut/<string:filename>')
_api.add_resource(TestAPI,'/gfsTestAPI/<string:filename>')
