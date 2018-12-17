# -*- coding: utf-8 -*-
# @Author: Charlie Gallentine
# @Date:   2018-12-17 12:44:03
# @Last Modified by:   Charlie Gallentine
# @Last Modified time: 2018-12-17 13:17:00
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:section_id>', views.prof_section, name='prof_section'),
	path('create', views.prof_create, name='prof_section_create'),
	path('<int:section_id>/edit', views.prof_edit, name='prof_section_edit'),
]