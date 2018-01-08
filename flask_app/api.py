#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/23
# @Author  : kingsley kwong
# @Site    :
# @File    : api.py
# @Software: flask_app
# @Function:

from flask import jsonify,abort,request
from flask_app import _api,_pool,app,logger
from flask_restful import Resource
from flask_app.tasks import files,web,mega_task,get_fs
import redis
import datetime
import json
import six
import shutil
import gridfs

_r = redis.Redis(connection_pool=_pool)
FileDequeue = []

#
# def prefix_url(json):
#     if type(json) is list:
#         for item in json:
#             prefix_url(item)
#     if type(json) is dict:
#         for items in json.items():
#             if 'url' in items:
#                 items = list(items)
#                 items[1] = "base_url_/" + items[1]
#                 lst = list()
#                 lst.append(items)
#                 items = dict(lst)
#                 json.update(items)
#             else:
#                 prefix_url(items[1])
#
# def GFS_Decorator(func):
#     def wrapper(self,col_name,file_name):
#         __db = _client[col_name]
#         self._fs = gridfs.GridFS(__db)
#         self._bucket = gridfs.GridFSBucket(__db)
#         return func(self,col_name,file_name)
#     return wrapper
#
#
# class Base(object):
#     _fs = gridfs.GridFS(_client.get_database())
#     _bucket = gridfs.GridFSBucket(_client.get_database())
#
class ListFile(Resource):
    @logger
    def get(self,col_name):
        fs = get_fs(col_name)[0]
        return fs.list()

class GetFileData(Resource):
    def get(self,col_name,file_name):
        return

# class DeleteFile(Resource,Base):
#     def get(self,col_name,file_name):
#         ret = files.delete_file.delay(col_name,file_name)
#         return jsonify(ret.get())
#




class SaveFile(Resource):
    #文件储存
    @logger
    def put(self,col_name,file_name):
        try:
            f = request.files.get('file')   #获取文件句柄
            # if pcm.available:     #内存缓存
            #     s = six.BytesIO()
            #     try:
            #         shutil.copyfileobj(f.stream,s)
            #     except MemoryError:
            #         s.close()
            #         f.close()
            #         raise MemoryError
            names = ['./flask_app/tmp/',
                     str(datetime.datetime.now().strftime("%Y%M%S")),
                     str(id(f))[3:],f.filename]
            s = open(''.join(names),'w+b')
            f.save(s)
            file_dict = dict(zip(['filename','bucket','contentType','fileobj'],
                    [f.filename,get_fs(col_name)[1],f.content_type,s]))
            FileDequeue.append(file_dict)  #添加到队列
        except Exception as e:
            print(e)
            s.close()
        finally:
            f.close()

    #文件进度
    def post(self,col_name,file_name):
        print('json file',request.get_json())
        return

_api.add_resource(ListFile,'/gfsList/<string:col_name>')
_api.add_resource(GetFileData,'/gfsGet/<string:col_name>/<string:file_name>')
# _api.add_resource(DeleteFile,'/gfsDel/<string:col_name>/<string:file_name>')
_api.add_resource(SaveFile,'/gfsSave/<string:col_name>/<string:file_name>')
