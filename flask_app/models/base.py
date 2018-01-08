#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    : 
# @File    : base.py
# @Software: 
# @Function:
from flask_app import _db




class BaseType(_db.Model):

    __abstract__ = True

    def add (self):
        return _db.session.add(self)

    def commit(self):
        return _db.session.commit()

    def delete(self):
        return _db.session.delete(self)



