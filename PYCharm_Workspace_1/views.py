#coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.http import HttpResponse, Http404
import datetime
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response

def hello(request):
    #return HttpResponse('Hello World!')
    return HttpResponse("客户端路径是 %s" % request.path)

def ua(request):
    # try:
    #     ua = request.META['HTTP_USER_AGENT']
    # except KeyError:
    #     ua = 'unknown'
    # return HttpResponse('您的浏览器是：%s' % ua)
    ua = request.META.get('HTTP_USER_AGENT','unknown')
    return HttpResponse('您的浏览器是：%s' % ua)

def current_datetime(request):
    current_date = datetime.datetime.now()
    #return render_to_response('current_datetime.html',{'now':now})
    return render_to_response('current_datetime.html', locals())
    #t = get_template('current_datetime.html')
    #c = Context({'now':now})
    #html = t.render(c)
    #html = "<html><body>It is now % s.</body></html>" % now
    #return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #return render_to_response('hours_ahead.html',{'offset':offset,'dt':dt})
    return render_to_response('hours_ahead.html', locals())
    #t = get_template('hours_ahead.html')
    #c = Context({'offset':offset,'dt':dt})
    #html = t.render(c)
    #html = "<html><body>In %s, time is %s.</body></html>" % (offset, dt)
    #return HttpResponse(html)