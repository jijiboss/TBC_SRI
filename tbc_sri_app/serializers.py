from rest_framework import serializers
from .models import lnos_statusPipeLine

"""
    Serializers allow to re-format data into a transferable format
    Also handles the POST and the PUT actions. See the link below
    http://www.django-rest-framework.org/tutorial/1-serialization/#creating-a-serializer-class

    A shortcut for creating serializer classes
        - An automatically determined set of fields.
        - Simple default implementations for the create() and update() methods.


    SERIALIZING

        serializer = MySerializer(inData)
        serliazlier.data
            <= this will be the Python native data type inData {'pk': 1, 'mbol': 'abc123'}
        content = JSONRenderer().render(serlizer.data)
            <= this will be the JSON version '{"pk": 1,"mbol": "abc123"}'

    DESERIALIZING

        from django.utils.six import BytesIO

    #parse a stream into Python native data types
        stream = BytesIO(content)
        data = JSONParser().parse(stream)

    #restore this into a fully populated object instance
        serializer = MySerializer(data = data)
        serliazlier.is_valid()
        serializer.validated_data
            <= This returns OrderedDict([('mbol', ' abc123')])
        serializer.save()
            <= This returns <InData: InData object>


    INSPECTING THE FIELDS

    >>> from tbc_sri_app.serializers import lnosStatusPipeLineSerializer

    >>> serializer = lnosStatusPipeLineSerializer
    >>> print(repr(serializer))
    <class 'tbc_sri_app.serializers.lnosStatusPipeLineSerializer'>

    >>> serializer = lnosStatusPipeLineSerializer()
    >>> print(repr(serializer))
    lnosStatusPipeLineSerializer():
        pk = IntegerField(label='ID', read_only=True)
        mbol = CharField(allow_blank=True, max_length=24, required=False)
        container = CharField(allow_blank=True, max_length=24, required=False)
"""

class lnosStatusPipeLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = lnos_statusPipeLine #model i am trying to serialize
        fields = ('pk', 'mbol', 'hbol', 'container', 'pol', 'vessel_departure', 'destination', 'vessel_arrival', 'carrier', 'vessel') #what attributes to return upon request
#        fields = ('mbol', 'container') #what attributes to return upon request
        #fields = '__all__' #or return everything
