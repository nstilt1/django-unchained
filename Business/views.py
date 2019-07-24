#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from . import models
from . import serializers

# Create your views here.

class BusinessViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Businesses to be viewed or edited
    '''
    queryset = models.Business.objects.all()
    serializer_class = serializers.BusinessSerializer
