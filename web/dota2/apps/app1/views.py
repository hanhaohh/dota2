from django.shortcuts import render
from django.shortcuts import render_to_response
def dashboard(request,template_name):
    return render_to_response(template_name,{"app":"app1"})
