#coding:utf-8

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(min_length=2,max_length=20,label='主题')
    email = forms.EmailField(required=False,label='收件人')
    message = forms.CharField(widget=forms.Textarea,label='正文')

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message)
        if num_words < 4:
            raise forms.ValidationError('填写的字数不够！')
        return message