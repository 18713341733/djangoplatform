
from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.contrib import messages


def home(request):
    return render(request,"KunYuanHome.html")


def deleteSql(request):
    return render(request,"deleteSql.html")

def deleteForm(request):
    return render(request,"deleteSql2.html")

def inputIphoneNumber(request):
    dic = dict(request.POST)
    print(dic)
    # return redirect(request.META['deleteSql.html'])
    # return redirect('http://www.baidu.com') # 重定向到新页面
    # return redirect('/deleteSql/',contextvars="abc")  # 重定向到新页面
    return render(request,"deletesql.html",context={
        "result":"success",
    })

def inputIphoneNumber2(request):
    dic = dict(request.POST)
    print(dic)
    # return redirect(request.META['deleteSql.html'])
    # return redirect('http://www.baidu.com') # 重定向到新页面
    # return redirect('/deleteSql/',contextvars="abc")  # 重定向到新页面
    return render(request,"deletesql2.html",context={
        "result":"success",
    })







#404页面
@csrf_exempt
def page_not_found(request):
    return render_to_response('404.html')

