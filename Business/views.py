#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action, api_view, permission_classes
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

    

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class BusinessViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Businesses to be viewed or edited
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = models.Business.objects.all()
    serializer_class = serializers.BusinessSerializer

    def delete(self, request, pk, format=None):
        if(IsAdminUser):
            business_delete = self.get_object(pk)
            business_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Employees to be viewed or edited
    '''
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

    

class BusinessEmployeeViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Business Employees to be viewed or edited
    maybe
    '''
    permission_classes = (IsAuthenticatedOrReadOnly)


    queryset = models.BusinessEmployee.objects.all()
    serializer_class = serializers.BusinessEmployeeSerializer

    '''
    

{"title": "BlockBuster",
        "description": "f",
        "address": "RIP Avenue",
        "employees_of_company": [
            {
                "first_name": "Johnny",
                "last_name": "Test",
                "email": "oawfj@aoj.com"
            },
           {
                "first_name": "Jimmy",
                "last_name": "Test",
                "email": "oawfj@aoj.com"
            }
        ]
}
'''