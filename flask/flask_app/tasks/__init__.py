#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

from flask_app import _cel
import celery

class BaseTask(celery.Task):pass
    # def on_failure(self, exc, task_id, args, kwargs, einfo):
    #     pass
    # def on_retry(self, exc, task_id, args, kwargs, einfo):
    #     pass