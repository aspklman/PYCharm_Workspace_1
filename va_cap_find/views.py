from django.shortcuts import render, render_to_response

# Create your views here.
def va_cap_find(request):
    return render_to_response('va_cap_find/cap_find.html')

# def cap_a(request):
#     return render_to_response('va_cap_find/cap_a.jpg')
#
# def cap_b(request):
#     return render_to_response('va_cap_find/cap_b.jpg')