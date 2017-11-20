#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

from flask_app.tasks import _cel,BaseTask



@_cel.task(base=BaseTask)
def test(a,b):

    return a + b