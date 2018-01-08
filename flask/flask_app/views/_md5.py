#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    : _md5.py
# @Software: flask_app
# @Function:


import hashlib


def MD5(str):
    str = str.encode('utf-8')
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

