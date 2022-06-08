"""KunYuanJiJin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from deleteSqlApp import views

from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^home/$',views.home), # 添加home/配置路径
    url(r'^$',views.home), # 添加home/配置路径
    url(r'^deleteSql/$',views.deleteSql),
    url(r'^inputIphoneNumber/$',views.inputIphoneNumber),
    url(r'^deleteForm/$',views.deleteForm),
    # url(r'^inputIphoneNumber2/$',views.inputIphoneNumber2),


]

handler404=views.page_not_found
