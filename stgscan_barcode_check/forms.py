#coding:utf-8

from django import forms
import winsound
from .models import *
import winsound

class BarcodeCheckForm(forms.Form):
    codef = forms.CharField(required=True,min_length=12,max_length=12,label='工厂条码')
    codec = forms.CharField(required=True,min_length=20,max_length=20,label='客户条码')
    # scan = forms.CharField(min_length=12,max_length=20,label='扫描')
    # scan1 = forms.CharField(min_length=12, max_length=12, label='扫描1')
    # scan2 = forms.CharField(min_length=20, max_length=20, label='扫描2')

    def clean_codef(self):
        codef = self.cleaned_data['codef']
        num_words = len(codef)
        if num_words == 12:
            # 检查【工厂条码】是否错误
            outboxd = Outboxd.objects.filter(fact_no__icontains='0006',outbox_no__icontains=codef)
            if not outboxd:
                winsound.Beep(300,600)
                raise forms.ValidationError('【工厂条码】错误，请检查！')
            # 检查是否有【入库扫描】
            stgscan_rec = Stgscan_rec.objects.filter(fact_no__icontains='0006',bar_no__icontains=codef)
            if not stgscan_rec:
                winsound.Beep(300,600)
                raise forms.ValidationError('未做【入库扫描】，请检查！')
            # 检查【工厂条码】是否重复扫描
            stgscan_barcode_check = Stgscan_barcode_check.objects.filter(fact_no__icontains='0006', cont_no__icontains=codef)
            if stgscan_barcode_check:
                winsound.Beep(300,600)
                raise forms.ValidationError('【工厂条码】重复扫描，请检查！')
        else:
            winsound.Beep(300, 600)
            # wavefile = "voice\cuowu.wav"
            # winsound.PlaySound(wavefile, 1)
            #winsound.PlaySound("SystemExit", 1)
            raise forms.ValidationError('条码长度错误！')
        return codef

    def clean_codec(self):
        codec = self.cleaned_data['codec']
        num_words = len(codec)
        if num_words == 20:
            # 检查【客户条码】是否错误
            odrsscc_pp_xml = Odrsscc_pp_xml.objects.filter(marknumberfrom__icontains=codec)
            if not odrsscc_pp_xml:
                winsound.Beep(300, 600)
                raise forms.ValidationError('【客户条码】错误，请检查！')
            # 检查【客户条码】是否重复扫描
            stgscan_barcode_check = Stgscan_barcode_check.objects.filter(fact_no__icontains='0006',bar_no__icontains=codec)
            if stgscan_barcode_check:
                winsound.Beep(300, 600)
                raise forms.ValidationError('【客户条码】重复扫描，请检查！')
            # 检查【工厂条码】与【客户条码】是否对应

        else:
            winsound.Beep(300, 600)
            # wavefile = "voice\cuowu.wav"
            # winsound.PlaySound(wavefile, 1)
            #winsound.PlaySound("SystemExit", 1)
            raise forms.ValidationError('条码长度错误！')
        return codec

    # def clean_scan(self):
    #     scan = self.cleaned_data['scan']
    #     num_words = len(scan)
    #     if num_words == 12 or num_words == 20:
    #         pass
    #     else:
    #         winsound.Beep(300, 600)
    #         # wavefile = "voice\cuowu.wav"
    #         # winsound.PlaySound(wavefile, 1)
    #         #winsound.PlaySound("SystemExit", 1)
    #         raise forms.ValidationError('条码长度错误！')
    #     return scan