#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

from flask_app.tasks import _cel,BaseTask,_client
import gridfs

def get_fs(db_name):
    __db = _client[db_name]
    _fs = gridfs.GridFS(__db)
    _bucket = gridfs.GridFSBucket(__db)
    return _fs,_bucket



@_cel.task(base=BaseTask)
def listing(db_name,file_name):
    _fs = get_fs(db_name)[0]
    return _fs.list()