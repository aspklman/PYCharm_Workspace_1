#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from django.shortcuts import render_to_response
from stgscan_barcode_check.forms import BarcodeCheckForm
from .models import *
from django.template import RequestContext
import winsound

def test(request):
    return render_to_response('stgscan_barcode_check/test.jsp')

def jquery(request):
    return render_to_response('stgscan_barcode_check/jquery.js')

def barcode_check(request):
    if request.method == 'POST':
        form = BarcodeCheckForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            fact_no = '0006'
            l = len(cd)
            s1 = cd['scan1']
            s2 = cd['scan2']
            # sku1 = '1'
            # sku2 = '2'
            # qty1 = 888
            # qty2 = 999
            # 获取【工厂条码】所对应的sku_number,qty
            # try:
            #     barcode_check_f = V_sis_sis_barcode_check_f.objects.get(fact_no=fact_no,ctn_no=s1)
            # except V_sis_sis_barcode_check_f.DoesNotExist:
            #     winsound.Beep(300, 600)
            #     return form
            #     # raise request.ValidationError('未做【入库扫描】，请检查！')
            barcode_check_f = V_sis_sis_barcode_check_f.objects.get(fact_no=fact_no, ctn_no=s1)
            sku1 = barcode_check_f.sku_number
            qty1 = barcode_check_f.qty
            # 获取【客户条码】所对应的sku_number,qty
            barcode_check_c = V_sis_sis_barcode_check_c.objects.get(fact_no=fact_no,ctn_no=s2)
            sku2 = barcode_check_c.sku_number
            qty2 = barcode_check_c.qty
            # 检查【工厂sku_number】、【工厂qty】与【客户sku_number】、【客户qty】是否相同
            # global sku1
            # global qty1
            # global sku2
            # global qty2
            if sku1 == sku2 and qty1 == qty2:
                return render_to_response('stgscan_barcode_check/barcode_check_true.html', {'form': form})
                # return render_to_response('stgscan_barcode_check/barcode_check_true.html',{'status': '正确'},context_instance=RequestContext(request, processors=[custom_proc]))
            else:
                return render_to_response('stgscan_barcode_check/barcode_check_false.html', {'form': form})
        else:
            return render_to_response('stgscan_barcode_check/barcode_check.html', {'form': form})
                # return render_to_response('stgscan_barcode_check/barcode_check.html', {'status': '对应错误'})
            # return HttpResponse('工厂条码：' + cd['scan1'] + '<br>客户条码：' + cd['scan2'])
            # return HttpResponse('这是SKU')
    else:
        form = BarcodeCheckForm()
    return render_to_response('stgscan_barcode_check/barcode_check.html', {'form': form})

# def custom_proc(request):
#     if request.method == 'POST':
#         form = BarcodeCheckForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             return cd