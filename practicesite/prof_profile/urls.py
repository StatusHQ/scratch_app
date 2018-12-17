# -*- coding: utf-8 -*-
# @Author: Charlie Gallentine
# @Date:   2018-12-17 12:44:03
# @Last Modified by:   Charlie Gallentine
# @Last Modified time: 2018-12-17 12:47:18
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	path('', views.index, name='index'),
	path('prof_profile/', views.prof_section, name='prof_profile'),
]