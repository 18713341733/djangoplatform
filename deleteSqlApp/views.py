# -*- coding: UTF-8 -*-
import simplejson as simplejson
from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.contrib import messages
import re
import pymysql
import os
from deleteSqlApp.utils.YmlUtil import YmlUtil
from deleteSqlApp.utils.DeleteInfo import DeleteInfo


def home(request):
    return render(request,"KunYuanHome.html")


def deleteSql(request):
    return render(request,"deleteSql.html")

def deleteForm(request):
    return render(request,"deleteSql2.html")

def inputIphoneNumber(request):
    # 前端输入数据
    phone_numbers = request.POST['textarea']

    # TODO： 输入手机号码的校验




    # 读取数据库配置
    # 读取CRM,licai数据配置信息
    licai_path = os.path.abspath('.')+"/deleteSqlApp/conf/dbinfo/"+"licai.yml"
    # path = "/Users/zhaohui/PycharmProjects/KunYuan/KunYuanJiJin/deleteSqlApp/conf/dbinfo/licai.yml"
    result =DeleteInfo.delete_licai(licai_path)
    print(result.message)
    print(phone_numbers)
    if(phone_numbers==""):
        return render(request, "deleteSql.html", context={
            "content": "输入不能为空",
        })

    if int(phone_numbers) > 5:
        return render(request, "deleteSql.html", context={
            "result": "成功",
            "content": phone_numbers,
        })
    else:
        return render(request, "deleteSql.html", context={
            "result": "失败",
            "reason": result.message,
            "content": phone_numbers,
        })







#404页面
@csrf_exempt
def page_not_found(request):
    return render_to_response('404.html')

if __name__ == '__main__':
    path = os.path.abspath('.') + "/conf/dbinfo/" + "licai.yml"
    print(path)

