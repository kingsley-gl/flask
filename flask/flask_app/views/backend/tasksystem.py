#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

from flask import *
from .import __modules

tasksystem = Blueprint('tasksystem', __name__)

@tasksystem.route('/tasksystem',methods=['GET','POST'])
def tasksystem():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		return render_template('tasksystem/task_system.html', headers = __modules)
	except KeyError:
		return redirect(url_for('home.login'))