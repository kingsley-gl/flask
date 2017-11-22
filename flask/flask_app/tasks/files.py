#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    : files.py
# @Software: flask_app.tasks
# @Function: put_file

from flask_app.tasks import _cel,BaseTask,get_fs
import json

__all__ = ['put_file','get_file_data']

@_cel.task(base=BaseTask)
def test(a,b):
    return a + b

@_cel.task(base=BaseTask)
def put_file(db_name,file):
    _fs = get_fs(db_name)[0]
    print(file.keys())
    if all(key in ['name','data'] for key in file.keys()):
        try:
            if file['name'] not in (file for file in _fs.list()):
                _fs.put(data=file['data'],filename=file['name'],encoding='utf-8')
                return {'state':'file new success'}
            else: return {'state':'file exists'}
        except Exception as e:
            return {'state':'file new error as %s' %e}

    else:
        return {'state':'file former error'}





@_cel.task(base=BaseTask)
def get_file_data(db_name,file_name):
    '''
    deal with small size files
    :param db_name:
    :param file_name:
    :return:
    '''
    _fs = get_fs(db_name)[0]
    try:
        file = _fs.find_one({'filename': file_name})
        string = file.read().decode('utf-8')
        data = json.loads(string)
    except ValueError:
        data = string
    finally:
        file.close()
    return data
@_cel.task(base=BaseTask)
def delete_file(db_name,file_name):
    _fs = get_fs(db_name)[0]
    _file = _fs.find_one({'filename':file_name})
    if not _file:
        return {'state': 'file not exist'}
    if _fs.exists(_file._id):
        ret = _fs.delete(_file._id)
        print(ret)
        return {'state':'file delete'}
    else:
        return {'state':'file not exist'}