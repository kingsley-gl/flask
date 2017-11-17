#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    : bim.py
# @Software:
# @Function:

from ..models.base import BaseType
from sqlalchemy import Column, String, create_engine, Integer

__all__ = ["DataModel"]

class DataModel(BaseType):
    # 表的名字:
    __tablename__ = 'datamodel'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    height = Column(Integer)
    length = Column(Integer)
    width = Column(Integer)
    size = Column(Integer)

    def __init__(self,name=None,height=None,length=None,width=None,size=None):
        self.name = name
        self.height = height
        self.length = length
        self.width = width
        self.size = size

    def __repr__(self):
    	return "<User(name=%s, height=%s, length=%s, width=%s, size=%s)>" %(self.name,self.height,self.length,self.width,self.size)