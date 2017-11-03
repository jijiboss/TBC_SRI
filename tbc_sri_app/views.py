from django.shortcuts import render
from django.template import loader
from .models import lnos_statusPipeLine
from django.forms import model_to_dict
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

def jquery01(request):
    return render(request, 'tbc_sri_app/jquery01.html')

def sritable3(request):
    #the model query object returning all contents
#    shipments = lnos_statusPipeLine.objects.all()
    shipments = model_to_dict(lnos_statusPipeLine.objects.all())
    #load in the template and create a variable as a reference to the template
    #template = loader.get_template('tbc_sri_app/sritable3.html')
    #dictionary to pass the model data with to the template
#    context = {'shipments': shipments}
    #render the template referenced by "context" variable passing it the "context" dictionary with data
    #return HttpResponse(template.render(context, request))
    return render(request, 'tbc_sri_app/sritable3.html', shipments)
#    return render(request, 'tbc_sri_app/sritable3.html', context)
