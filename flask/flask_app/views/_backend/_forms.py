#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/28
# @Author  : kingsley kwong
# @Site    :
# @File    : _forms.py
# @Software: flask_app
# @Function:

from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class PageForm(FlaskForm):
    PerPage = SelectField('PerPage',id="selector",coerce=int,default=5,choices =[(5,'5'),(10,'10'),(50,'50'),(100,'100')])

class TableForm(FlaskForm):
    Name = StringField('Name')
    Comment = StringField('Comment')
    Rows = IntegerField('Rows')
    CreateTime = DateTimeField('CreateTime')
