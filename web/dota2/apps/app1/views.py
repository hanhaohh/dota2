from django.shortcuts import render
from django.shortcuts import render_to_response
def hello(request):
    return render_to_response('app1.html',{"app":"app1"})
