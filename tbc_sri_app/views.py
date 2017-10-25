from django.shortcuts import render

#
from django.http import HttpResponse

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def helloWorld(request, namae):
    return HttpResponse("Hello world %s!" % namae)

def index(request):
    #add code here
    #https://docs.djangoproject.com/en/1.11/intro/tutorial03/#a-shortcut-render
    return render(request, 'tbc_sri_app/index.html')

def sritable(request):
    return render(request, 'tbc_sri_app/sritable.html')
