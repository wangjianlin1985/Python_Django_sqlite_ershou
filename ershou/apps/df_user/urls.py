#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url,re_path
from django.views.static import serve
from tiaozao_shop import settings
from .views import *
from . import viewsUtil

app_name = 'df_user'

urlpatterns = [
    url(r'^register/$', register, name="register"),
    url(r'^register_handle/$', register_handle, name="register_handle"),
    url(r'^register_exist/$', register_exist, name="register_exist"),
    url(r'^login/$', login, name="login"),
    url(r'^login_handle/$', login_handle, name="login_handle"),
    url(r'^info/$', info, name="info"),
    url(r'^order/(\d+)$', order, name="order"),
    url(r'^site/$', site, name="site"),
    url(r'^publishers/$',publishers,name="publishers"),
    url(r'^changeInformation/$',changeInformation,name="changeInformation"),
    url(r'^check_user/$',check_user,name="check_user"),
    url('^myself_information/$', myself_information, name="myself_information"),
    url('^shoper_information/(.+)/$', shoper_information, name="shoper_information"),
    url('^message/$', message, name="message"),
    url('^person_message/$', person_message, name="person_message"),
    #url(r'^kefu_message/$', kefu_message, name="kefu_message"),
    url(r'^logout/$', logout, name="logout"),
    #显示验证码
    url(r'^verify_show/$', verify_show,name="verify_show"),
    url(r'^verifycode/$', viewsUtil.verify_code,name="verifycode"),
    #修改密码
    url(r'^changeInPwd/$', changeInPwd,name="changeInPwd"),
    #重置密码
    url(r'^findpwdView/$', findpwdView,name="findpwdView"),
    #退货
    url(r'^tuihuo/$', tuihuo,name="tuihuo"),
    re_path('^media/(?P<path>.*)/$',serve,{'document_root':settings.MEDIA_ROOT}),
]