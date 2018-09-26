from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        message = '你要查找的是：%r' % request.GET['q']
    else:
        message = '你没有输入内容！'
    return render_to_response(message)
