from rest_framework import serializers
from .models import lnos_statusPipeLine

#Serializers allow to re-format data into a transferable format

class lnosStatusPipeLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = lnos_statusPipeLine #model i am trying to serialize
        fields = ('pk', 'mbol', 'container') #what attributes to return upon request
        #fields = '__all__' #or return everything
