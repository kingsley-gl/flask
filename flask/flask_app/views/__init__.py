#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/28
# @Author  : kingsley kwong
# @Site    : 
# @File    : _frontend.__init__.py
# @Software: flask_app
# @Function:

from ._backend import *
from ._frontend import *

_back_list = []
_front_list = []

for _module in dir(_backend):
    if _module[0] == '_':
        continue
    locals()[_module] = eval(_module)
    _back_list.append(_module)


for _module in dir(_frontend):
    if _module[0] == '_':
        continue
    locals()[_module] = eval(_module)
    _front_list.append(_module)


__all__ = _back_list + _front_list


