from django.shortcuts import render
from django.template import loader
#from django.forms import model_to_dict
#from django.http import HttpResponse #replaced by .Response
#from django.http import JsonResponse #replaced by .Response
from django.http import HttpRequest #https://docs.djangoproject.com/en/dev/ref/request-response/
from django.core import serializers
import json
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import lnos_statusPipeLine
from .serializers import lnosStatusPipeLineSerializer
#=================================
#for REST framework
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
#=================================
#for debugging
#https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/
#import pdb

#just for experimenting purposes. DO not use "csrf_exempt" in production
#from django.views.decorators.csrf import csrf_exempt
#=================================
def index(request):
    #add code here
    #https://docs.djangoproject.com/en/1.11/intro/tutorial03/#a-shortcut-render
    return render(request, 'tbc_sri_app/index.html')

def baseGeneric(request):
    return render(request, 'base_generic.html')
    
def sritable3(request):
    #load in the template and create a variable as a reference to the template
    template = loader.get_template('tbc_sri_app/sritable3.html')
    return render(request, 'tbc_sri_app/sritable3.html')


#I can test this method by calling this URL on the browser directly.
#if successful, i shoudl see the query results.
#To see if the data was returned to the calling HTML, go to the Network tab and look for the XHR entry.
#The Response tab will have the actual returned data, or "failure".
#Also can test out this query and result by tryin them on the python shell;
#   python manage.py shell
#Take 2 in attept to understand REST better
#http://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers
@api_view(['GET', 'POST'])
def myLoadData02(request):
    #List all existing or create new
    print("===============================================")
    if request.method == 'GET':
        cargo = lnos_statusPipeLine.objects.all()
        serializer = lnosStatusPipeLineSerializer(cargo, many = True)
        print("===============================================")
        #return JsonResponse(serializer.data, safe = False) #Replaced by .Response and @api_view
        return Response(serializer.data)

    elif request.method == 'POST':
        #JSONParser() => parse request content that is in JSON format
        #.parse(request) => parse stream-like object representing the body of the request
        #http://www.django-rest-framework.org/api-guide/parsers/#custom-parsers
        #parse the stream into Python native data type
        #then turn that into a dictionary of validated data
        print("LoadData:POST request => ", request)
        data = JSONParser().parse(request) #dict at this point
        print("LoadData:POST data => ", data)
        serializer = lnosStatusPipeLineSerializer(data = data)
        """
        #Supposedly no longer necessary to manually convert input stream into dict after using the api_view
        #instead simply call the serializer passing the request.data as below
        serializer = lnosStatusPipeLineSerializer(data=request.data)
        """
        print("LoadData:POST attempt => ", serializer)
        if serializer.is_valid():
            serializer.save()
            print("LoadData:POST successful => ", serializer)
            print("===============================================")
            #return JsonResponse(serializer.data, status = 201) #replaced by .Response and .status and @api_view
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        print("===============================================")
        #return JsonResponse(serializer.errors, status = 400) #replaced by .Response and .status and @api_view
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def myUpdateData02(request, pk):

    print("===============================================")
    """
        #Retrieve, update or delete
        Because I need to pass pk, need to update the JS with the following...
            var thisPK = item["pk"] //need to get the pk to pass with the PUT request
            ...
            url: 'myUpdateData02/' + thisPK,
            ...
        Then update urls.py accordingly
            url(r'^myUpdateData02/(?P<pk>[0-9]+)$', views.myUpdateData02, name='myUpdateData02'),
    """

    #try getting the 'pk' instance
    try:
        cargo = lnos_statusPipeLine.objects.get(pk = pk)
    #return Not Found 404 if not found
    except lnos_statusPipeLine.DoesNotExist:
        print("===============================================")
        #return HttpResponse(status = 404) #replaced by .Response and .status and @api_view
        return Response(status = status.HTTP_404_NOT_FOUND)

    #GET
    if request.method == 'GET':
        #Serializer will return the instance object in Python native format
        serializer = lnosStatusPipeLineSerializer(cargo)
        #Return JSON-fied representation of the instance data
        print("===============================================")
        #return JsonResponse(serializer.data) #replaced by .Response and @api_view
        return Response(serializer.data)

    #PUT
    elif request.method == 'PUT':

        #JSONParser() => parse request content that is in JSON format
        #.parse(request) => parse stream-like object representing the body of the request
        #parse the stream into Python native data type
        #then turn that into a dictionary of validated data
        #LoadData:PUT attempt =>  {'pk': 25, 'mbol': 'mbol01', 'container': 'container02'}
        #this updates fine
        data = JSONParser().parse(request) #dict at this point
        print("LoadData:PUT attempt => ", data)
        serializer = lnosStatusPipeLineSerializer(cargo, data = data)

        """
        #Supposedly no longer necessary to manually convert input stream into dict after using the api_view
        #But this does not update as expected.
        #request.data returns a QueryDict instead of a dict
        serializer = lnosStatusPipeLineSerializer(cargo, data = request.data)
        print("LoadData:PUT attempt => ", request.data)
        #LoadData:PUT attempt =>  <QueryDict: {'{"pk":25,"mbol":"mbol01","container":"container02"}': ['']}>
        #Tried dict(request.data) which would pass this
        #LoadData:PUT attempt =>  {'{"pk":25,"mbol":"mbol01","container":"container02"}': ['']}
        """

        if serializer.is_valid():
            serializer.save()
            print("UpdateData:PUT successful => ", serializer.data)
            print("===============================================")
            #return JsonResponse(serializer.data)  #replaced by .Response and @api_view
            return Response(serializer.data)
        print("===============================================")
        #return JsonResponse(serializer.errors, status = 400)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cargo.delete()
        print("===============================================")
        #return HttpResponse(status = 204) #replaced by .Response and .status and @api_view
        return Response(status = status.HTTP_204_NO_CONTENT)
