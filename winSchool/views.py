from django.shortcuts import render_to_response
from django.template import RequestContext
from winSchool.models import User

def home(request):
    return render_to_response(
        'index.html', {}, context_instance=RequestContext(request))

def register(request):
    user_name=request.POST['user_name']
    password=request.POST['pass']
    user = User(name=user_name)
    user.save()
    return render_to_response(
        'index.html',{'message':'success'}, context_instance=RequestContext(request))
