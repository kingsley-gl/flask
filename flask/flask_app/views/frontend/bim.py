#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/11
# @Author  : kingsley kwong
# @Site    :
# @File    : bim.py
# @Software:
# @Function:


from flask_app.models.bim import DataModel
from flask import Blueprint, request,jsonify






bim = Blueprint('bim', __name__, url_prefix='/bim')

re_dict = lambda str1,str2,str3,str4=None:{'code':str1,'state':str2,'statement':str3,'data':str4}

@bim.route('/model', methods=['GET','POST'])
def model():
    if request.method == 'POST':
        m = DataModel()
        data_lst = m.query().all()
        print(data_lst)
        json_list = []
        for data in data_lst:
            record = {}
            for key in data.__dict__.keys():
                if key in '_sa_instance_state':
                    continue
                record.update({key:data.__dict__[key]})
            json_list.append(record)
        result = re_dict('01','True','Data return successed!',json_list)
        return jsonify(result)