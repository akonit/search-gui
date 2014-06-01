from django.http import HttpResponse
from django.shortcuts import render

from news.models import News

def index(request):
    encoding = 'cp1251'
    return render(request, 'news/index.html')

def search(request):
    if 'query' in request.GET and request.GET['query'] and 'page' in request.GET and request.GET['page']:
        query = request.GET['query']
        page = request.GET['page']
        # send request to pipe
        # get result from pipe
        # render result
        return render(request, 'news/search.html')
    else :
        return render(request, 'news/index.html')