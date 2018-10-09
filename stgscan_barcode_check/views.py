#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from django.shortcuts import render_to_response
from stgscan_barcode_check.forms import BarcodeCheckForm

def barcode_check(request):
    if request.method == 'POST':
        form = BarcodeCheckForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            # return HttpResponse('工厂条码：' + cd['codef'] + '<br>客户条码：' + cd['codec'])
            # return HttpResponse(cd['scan'])
    else:
        form = BarcodeCheckForm()
    return render_to_response('stgscan_barcode_check/barcode_check.html', {'form':form})