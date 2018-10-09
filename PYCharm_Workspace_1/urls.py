"""PYCharm_Workspace_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import include, url
from django.contrib import admin
from PYCharm_Workspace_1.views import hello, current_datetime, hours_ahead, ua, display_meta
from books.views import search_form, search
from contact.views import contact, thanks, my_image, unruly_passengers_csv, hello_pdf
from contact.forms import ContactForm
#from account.views import login_view
from django.contrib.auth.views import login, logout
from users.views import index
from gdpdata.views import gdpdata
from stgscan_barcode_check.views import barcode_check

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^hello/$',hello),
    url(r'^time/$',current_datetime),
    url(r'^datetime/$',current_datetime),
    url(r'^plus/(\d{1,2})/$',hours_ahead),
    url(r'^ua/$',ua),
    url(r'^display_meta/$', display_meta),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
    url(r'^contact/$', contact),
    url(r'^thanks/$', thanks),
    url(r'^my_image/$', my_image),
    url(r'^unruly_passengers_csv/$', unruly_passengers_csv),
    url(r'^hello_pdf/$', hello_pdf),
    #url(r'^accounts/login/$', login),
    #url(r'^accounts/logout/$', logout),
    url(r'^users/', include('users.urls',namespace="users")),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^gdpdata/$', gdpdata),
    url(r'^barcode_check/$', barcode_check),
]