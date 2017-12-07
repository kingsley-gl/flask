#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/28
# @Author  : kingsley kwong
# @Site    :
# @File    : _forms.py
# @Software: flask_app
# @Function:

from flask_wtf import FlaskForm
from wtforms.validators import *

class Base(FlaskForm):

    @classmethod
    def create_field(cls,field_name,field_type):
        #auto create field
        try:
            import wtforms
            if field_type in wtforms.validators.__all__:
                setattr(cls, field_name, eval(field_type+'()'))
            else:
                raise "field type not in validators"
        except Exception as e:
            raise e




class TableForm(Base):
    pass


