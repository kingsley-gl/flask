#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    : mega_task.py
# @Software: flask_app.tasks
# @Function:

from flask_app.tasks import _cel,BaseTask

__all__ = ['put_mega_file']

@_cel.task(base=BaseTask)
def put_mega_file():
    pass