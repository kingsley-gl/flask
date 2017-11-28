#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

from flask import *
import sys

filesystem = Blueprint('filesystem', __name__)
#header register
__func = [{'file_system':'system'},]
# {function_name:chinese_name}

@filesystem.route('/filesystem',methods=['GET','POST'])
def file_system():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		return render_template('filesystem/file_system.html', headers = __func,module='filesystem')
	except KeyError:
		return redirect(url_for('home.login'))
