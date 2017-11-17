#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    : 
# @File    : 
# @Software: 
# @Function:
from flask_app import app
from flask_cors import *
from werkzeug.contrib.fixers import ProxyFix


if __name__ == '__main__':
	app.wsgi_app = ProxyFix(app.wsgi_app)
	CORS(app,supports_credentials=True)
	app.run(host='localhost',port=8000)
