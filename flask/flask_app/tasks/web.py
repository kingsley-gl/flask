#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    : web.py
# @Software: flask_app.tasks
# @Function:

from flask_app.tasks import _cel,BaseTask,_client,get_fs

__all__ = ['list_file']


@_cel.task(base=BaseTask)
def list_file(col_name):
    _fs = get_fs(col_name)[0]
    return _fs.list()