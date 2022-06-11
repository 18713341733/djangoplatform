# -*- coding: UTF-8 -*-
import simplejson as simplejson
from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from deleteSqlApp.utils.CheckPhoneNumber import CheckPhoneNumber




def home(request):
    return render(request,"Home.html")


def deleteSql(request):
    return render(request,"deleteSql.html")

def deleteForm(request):
    return render(request,"deleteSql.html")

def inputIphoneNumber(request):
    # 前端输入数据

    try:
        phone_numbers = request.POST['textarea']
    except:
        return render(request, "deleteSql.html")

    print("phone_numbers:"+phone_numbers)

    # TODO： 输入手机号码的校验
    result,messages = CheckPhoneNumber.check_phone_number(phone_numbers)
    print("result:"+result)
    if result == "False":
        return render(request, "deleteSql.html", context={
            "result": "失败",
            "content": phone_numbers,
        })
    liststr = "".join(messages)
    messages = "成功处理以下数据:"+liststr
    return render(request, "deleteSql.html", context={
        "result": "成功",
        "content": phone_numbers,
        "mymessages":messages,
    })











#404页面
@csrf_exempt
def page_not_found(request):
    return render_to_response('404.html')

