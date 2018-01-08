#!/bin/bash
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    :
# @Software:
# @Function:

echo "===========start flask gunicorn========"
gunicorn -w 8 -b 192.168.1.172 manage.run:app
