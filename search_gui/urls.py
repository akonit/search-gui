# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from news import views

urlpatterns = patterns('',
    url(r'^news/', include('news.urls')),
)
