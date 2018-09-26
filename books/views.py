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
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('请输入要查找的书籍名称!')
        elif len(q) > 10:
            errors.append('不能超过10个字！')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html', {'books':books,'query':q})
        return render_to_response('search_form.html', {'errors':errors})
