#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    : __init__.py
# @Software: flask_app.tasks
# @Function:

from flask_app import _cel,_mongo
import celery
import gridfs

__all__ = ['BaseTask']

def get_fs(col_name):
    __db = _mongo.get_database()
    _fs = gridfs.GridFS(__db,col_name)
    _bucket = gridfs.GridFSBucket(__db,col_name)
    return _fs,_bucket

class BaseTask(celery.Task):

    def on_success(self, retval, task_id, args, kwargs):
        print('task done: %s' %retval)
        return super(BaseTask,self).on_success(retval, task_id, args, kwargs)
    # def after_return(self, status, retval, task_id, args, kwargs, einfo):
    #     pass
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task raise except: %s, except info: %s' %(exc,einfo))
        return super(BaseTask,self).on_failure(exc,task_id,args,kwargs,einfo)
    # def on_retry(self, exc, task_id, args, kwargs, einfo):
    #     pass
