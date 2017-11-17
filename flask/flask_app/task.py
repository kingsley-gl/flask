#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:
# from .cel_manage import cel
from flask_app import _cel



@_cel.task()
def test(a,b):
    return a + b

