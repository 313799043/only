"""APP01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include,re_path
from django.conf.urls import url, include
from APP01.settings import MEDIA_ROOT
from django.views.static import serve





# import xadmin
from users.views import IndexView,LoginView,RegisterView,AciveUserView,LogoutView


app_name='users','organization',

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('xadmin/', xadmin.site.urls),
    #主页
    # url('110/', IndexView.as_view(), name="index"),
    path('', IndexView.as_view(), name=  "index"),
    #注册
    url('^register/$', RegisterView.as_view(), name="register"),
    #验证码
    url(r'^captcha/', include('captcha.urls')),
    #激活
    url(r'^active/(?P<active_code>.*)/$', AciveUserView.as_view(), name="user_active"),
    # 登录
    url('^login/$', LoginView.as_view(), name="login"),
    #退出登录
    url('^logout/$', LogoutView.as_view(), name="logout"),
    # 配置上传文件的访问处理函数
    # url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # 课程机构url配置
    url(r'^org/', include('organization.urls', namespace="org")),
    # url(r'^org_list/',OrgView.as_view() , name="org_list"),
    #配置users



    path("users/", include('users.urls', namespace="users")),



    # 课程app的url配置
    path("course/", include('courses.urls', namespace="course")),


    # url(r'^ueditor/',include('DjangoUeditor.urls' )),
    # path('ueditor/', include('DjangoUeditor.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
]
