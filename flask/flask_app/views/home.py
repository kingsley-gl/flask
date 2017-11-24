#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    : 
# @File    : 
# @Software: 
# @Function:

from flask import Blueprint,render_template

home = Blueprint('home', __name__)


@home.route('/',methods=['GET','POST'])
def index():
	return render_template('login.html')

@home.route('/test',methods=['GET','POST'])
def test():
	return render_template('index.html')