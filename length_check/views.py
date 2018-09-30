from django.shortcuts import render, render_to_response
from length_check.models import Test

# Create your views here.
def search_test(request):
    test = Test.objects.filter(country__icontains='China')
    return render_to_response('test/test.html', {'test':test})