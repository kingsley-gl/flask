#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

from flask import *

sqlsystem = Blueprint('sqlsystem', __name__)
#header register
__func = [
			# {function_name:chinese_name},
			{'detail':'xiangqing'},
		  	{'db_list':'shujukuliebiao'},
			{'opration':'shujukucaozuo'}
		]


@sqlsystem.route('/detail',methods=['GET','POST'])
def detail():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		return render_template('sqlsystem/detail.html', headers = __func,module='sqlsystem')
	except KeyError:
		return redirect(url_for('home.login'))

@sqlsystem.route('/db_list',methods=['GET','POST'])
def db_list():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		return render_template('sqlsystem/db_list.html', headers=__func, module='sqlsystem')
	except KeyError:
		return redirect(url_for('home.login'))

@sqlsystem.route('/opration',methods=['GET','POST'])
def opration():
	try:
		if not session['logged_in']:
			return redirect(url_for('home.login'))
		return render_template('sqlsystem/opration.html', headers=__func, module='sqlsystem')
	except KeyError:
		return redirect(url_for('home.login'))