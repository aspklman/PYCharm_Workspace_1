#coding:utf-8

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(min_length=2,max_length=20)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    # def clean_message(self):
    #     message = self.cleaned_data['message']
    #     num_words = len(message.split())
    #     if num_words < 4:
    #         raise forms.ValidationError('填写的字数不够！')
    #     return message