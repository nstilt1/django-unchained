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
class EmployeeViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Employees to be viewed or edited
    '''
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
class BusinessWmployeeViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Business Employees to be viewed or edited
    maybe
    '''
    queryset = models.BusinessEmployee.objects.all()
    serializer_class = serializers.BusinessEmployeeSerializer