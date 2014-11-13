from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def dashboard(request,template_name):
    if  request.user.is_authenticated():
        username = request.user
        return render_to_response(template_name,{"username":username})
    else:
        return HttpResponseRedirect('/login/')
