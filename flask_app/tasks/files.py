#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    : files.py
# @Software: flask_app.tasks
# @Function: put_file

from flask_app.tasks import _cel,BaseTask
import json

__all__ = ['put_file','get_file_data']




# @_cel.task(base=BaseTask)
# def get_file_data(col_name,file_name):
#     '''
#     deal with small size files
#     :param col_name: collection name
#     :param file_name:
#     :return:
#     '''
#     _fs = get_fs(col_name)[0]
#     try:
#         file = _fs.find_one({'filename': file_name})
#         string = file.read().decode('utf-8')
#         data = json.loads(string)
#     except ValueError:
#         data = string
#     finally:
#         file.close()
#     return data
# @_cel.task(base=BaseTask)
# def delete_file(col_name,file_name):
#     _fs = get_fs(col_name)[0]
#     _file = _fs.find_one({'filename':file_name})
#     if not _file:
#         return {'state': 'file not exist'}
#     if _fs.exists(_file._id):
#         ret = _fs.delete(_file._id)
#         print(ret)
#         return {'state':'file delete'}
#     else:
#         return {'state':'file not exist'}