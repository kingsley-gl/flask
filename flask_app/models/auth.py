#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    : 
# @File    : auth.py
# @Software: 
# @Function:

from ..models.base import BaseType
from sqlalchemy import Column, String, Integer

__all__=["User"]

class User(BaseType):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    password = Column(String(255))
    privileges = Column(Integer)

    def __init__(self,name=None,password=None,privileges=None):
        self.name = name
        self.password = password
        self.privileges = privileges

    def __repr__(self):
    	return "<User(name=%s,password=%s, privileges=%s)>" %(self.name,self.password,self.privileges)


