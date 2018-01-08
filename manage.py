#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    : 
# @File    : manage.py
# @Software: flask
# @Function:
import threading,os
from flask_app import app
from flask_cors import *
from werkzeug.contrib.fixers import ProxyFix
from multiprocessing import Process
from flask_app.worker import thread_pool

def celery_start ():
	app.logger.info("----------starting celery serve----------")
	#print("----------starting celery serve----------")
	os.system('py -3 -m celery -A flask_app.tasks worker -Q mega_task,files,web')

if __name__ == '__main__':
	p = Process(target=celery_start)
	p.start()
	for item in thread_pool:
		item.start()
	app.wsgi_app = ProxyFix(app.wsgi_app)
	CORS(app, supports_credentials=True)
	app.run(host='192.168.0.100', port=8000)

