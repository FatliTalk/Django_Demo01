"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from firstapp.views import index, detail, detail_comment # 从firstapp包中的views模块中导入index、detail、detail_comment视图函数

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', index, name='index'), # 添加的代码
    # 用URL正则实现文章链接跳转|自动设置URL文章页数
    # 文章页数参数设置为page_num，另命名为P。注：数据库会自动给每篇文章添加对应页数。
    # “d+”：digital+是正则表达-页数可为不限制多位数的意思
    # "$"为正则表达，结束、到此为止的意思
    # 最后，回到视图层views.py添加参数page_num，告诉视图层页数参数是从urls.py传递过去的。
    url(r'^detail/(?P<page_num>\d+)$', detail, name='detail'), # 添加的代码(评论页面)
	# 视图层views.py中实现了文章视图和评论表单视图分离，需要分配新的url给分离后的评论表单视图
	url(r'^detail/(?P<page_num>\d+)/comment$', detail_comment, name='comment'),
]
