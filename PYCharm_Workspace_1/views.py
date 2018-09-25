from django.http import HttpResponse, Http404
import datetime
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse('Hello World!')

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