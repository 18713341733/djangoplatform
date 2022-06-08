import simplejson as simplejson
from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.contrib import messages
import re


def home(request):
    return render(request,"KunYuanHome.html")


def deleteSql(request):
    return render(request,"deleteSql.html")

def deleteForm(request):
    return render(request,"deleteSql2.html")

def inputIphoneNumber(request):
    phone_numbers = request.POST['textarea']
    print(phone_numbers)
    if int(phone_numbers) > 5:
        return render(request, "deleteSql.html", context={
            "result": "成功"
        })
    else:
        return render(request, "deleteSql.html", context={
            "result": "失败"})







#404页面
@csrf_exempt
def page_not_found(request):
    return render_to_response('404.html')

