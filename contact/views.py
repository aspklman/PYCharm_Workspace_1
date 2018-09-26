#coding:utf-8

from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render_to_response

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('请输入邮件主题！')
        if not request.POST.get('message',''):
            errors.append('请输入邮件内容！')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('请输入邮件地址！')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get['email','562142139@qq.com'],
                ['562142139@qq.com'],
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        return render_to_response('contact_form.html',{'errors':errors})

def thanks(request):
    return HttpResponse('谢谢您的邮件！我们会尽快处理！')