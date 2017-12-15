#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/28
# @Author  : kingsley kwong
# @Site    :
# @File    : filesystem.py
# @Software: flask_app
# @Function:

from flask import *
from flask_app import _client

filesystem = Blueprint('filesystem', __name__,url_prefix='/filesystem')
#header register
__func = [
			# {function_name:chinese_name},
			{'detail':'system'},
		]


@filesystem.route('/detail',methods=['GET','POST'])
def detail():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))

		print(_client)



		return render_template('filesystem/file_system.html',
							   headers = __func,
							   module='filesystem')
	except KeyError:
		return redirect(url_for('home.login'))
