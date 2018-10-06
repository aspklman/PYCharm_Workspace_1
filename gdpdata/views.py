from django.shortcuts import render, render_to_response
from gdpdata.models import Gdpdata

# Create your views here.
def gdpdata(request):
    country = Gdpdata.objects.all()      #filter(country__icontains='China')
    return render_to_response('test/test.html', {'country': country})