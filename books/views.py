#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book

# Create your views here.

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    # if 'q' in request.GET:
    #     message = '你要查找的是：%r' % request.GET['q']
    # else:
    #     message = '你没有输入内容！'
    # return HttpResponse(message)
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_result.html', {'books':books, 'query':q})
    else:
        HttpResponse('Please submit a search term.')
