#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/28
# @Author  : kingsley kwong
# @Site    :
# @File    : filesystem.py
# @Software: flask_app
# @Function:

from flask import *


filesystem = Blueprint('filesystem', __name__)
#header register
__func = [
			# {function_name:chinese_name},
			{'file_system':'system'},
		]


@filesystem.route('/filesystem',methods=['GET','POST'])
def file_system():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		return render_template('filesystem/file_system.html', headers = __func,module='filesystem')
	except KeyError:
		return redirect(url_for('home.login'))
