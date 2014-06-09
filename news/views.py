# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from news.models import News
from news.additional import JsonNews
import os, sys
import json
import math

# search request
wfPath = "./web_request"

# search results
rfPath = "./json_output"

news_per_page = 10

def index(request):
    request.encoding = 'utf8'
    return render(request, 'news/index.html')

def search(request):
    request.encoding = 'utf8'
    if 'query' in request.GET and request.GET['query'] and 'page' in request.GET and request.GET['page']:
        query = request.GET['query']
        page = request.GET['page']
        
        
        wp = open(wfPath, 'w')
        wp.write(query.encode('UTF-8'))       
        wp.close()

        # get result from pipe
        if not os.path.exists(rfPath):
            os.mkfifo(rfPath)

        rp = open(rfPath, 'r')
        response = rp.read().decode('cp1251')
        full_news_list = parseJsonResponse(eval(response))
        rp.close()
        
        news_list = getNewsPerPage(full_news_list, int(page))
        context = {'news_list': news_list, 'range' : range(1, getPageNumber(len(full_news_list)) + 1), 'query' : query}
        return render(request, 'news/search.html', context)
    else :
        return render(request, 'news/index.html')

# prepare request for html output
def parseJsonResponse(response):
    news_list = []
    for entry in response:
        try:
            news_id = entry[0]
            news = News.objects.get(id=news_id)
            news_json = eval(news.json)
            jsonNews = JsonNews()
            jsonNews.title = news_json['title']
            link = news_json['link']
            while link.find('\\') != -1:
                link = link.replace("\\", "")
            jsonNews.link = link
            jsonNews.source = news_json['source']
            jsonNews.region = news_json['region']
            jsonNews.branch = news_json['branch']
            jsonNews.date = news_json['date']
            jsonNews.snippet = entry[1]
            news_list.append(jsonNews)
        except:
            print 'oops(('
    return news_list

# get requested page content
def getNewsPerPage(full_news_list, page):
    start = (page - 1) * news_per_page
    end = page * news_per_page

    if end < 0:
        end = 0

    if end > len(full_news_list):
        end = len(full_news_list)

    return full_news_list[start : end]

 #count total page number
def getPageNumber(length):
    if length % news_per_page == 0:
        return length / news_per_page
    else:
        return length / news_per_page + 1
