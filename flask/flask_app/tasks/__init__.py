#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

from flask_app import _cel,_client
import celery


class BaseTask(celery.Task):

    def on_success(self, retval, task_id, args, kwargs):
        print('task done: %s' %retval)
        return super(BaseTask,self).on_success(retval, task_id, args, kwargs)
    # def after_return(self, status, retval, task_id, args, kwargs, einfo):
    #     pass
    # def on_failure(self, exc, task_id, args, kwargs, einfo):
    #     pass
    # def on_retry(self, exc, task_id, args, kwargs, einfo):
    #     pass
