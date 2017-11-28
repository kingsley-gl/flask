#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

from flask import *


tasksystem = Blueprint('tasksystem', __name__)
#header register
__func = [{'task_system':'system'}]
# {urlname:chinesename}


@tasksystem.route('/tasksystem',methods=['GET','POST'])
def task_system():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		return render_template('tasksystem/task_system.html', headers = __func,module='tasksystem')
	except KeyError:
		return redirect(url_for('home.login'))