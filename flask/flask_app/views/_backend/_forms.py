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

class Base(FlaskForm):

    @classmethod
    def create_field(cls,field_name,field_type):
        #auto create field
        try:
            import wtforms
            if field_type in wtforms.fields.__dict__:
                setattr(cls, field_name, eval(field_type+'("%s")' %field_name))
            else:
                raise "field type not in validators"
        except Exception as e:
            raise e




class TableForm(Base):
    # submit = SubmitField("operator")
    pass


