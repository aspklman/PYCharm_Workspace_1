#coding:utf-8

from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from contact.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', '562142139@qq.com'),
                ['562142139@qq.com'],
            )
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form':form})
    # errors = []
    # if request.method == 'POST':
    #     if not request.POST.get('subject',''):
    #         errors.append('请输入邮件主题！')
    #     if not request.POST.get('message',''):
    #         errors.append('请输入邮件内容！')
    #     if request.POST.get('email') and '@' not in request.POST['email']:
    #         errors.append('请输入邮件地址！')
    #     if not errors:
    #         send_mail(
    #             request.POST['subject'],
    #             request.POST['message'],
    #             request.POST.get('email','562142139@qq.com'),
    #             ['562142139@qq.com'],
    #         )
    #         return HttpResponseRedirect('/thanks/')
    # return render_to_response('contact_form.html',{
    #     'errors':errors,
    #     'subject':request.POST.get('subject',''),
    #     'message':request.POST.get('message',''),
    #     'email':request.POST.get('email',''),
    # })

def thanks(request):
    return render_to_response('thanks.html')