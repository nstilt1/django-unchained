from rest_framework import serializers
from . import models

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Employee
        fields = ['first_name', 'last_name', 'email', 'business', 'id']
    

class BusinessSerializer(serializers.ModelSerializer):
    #- the model itself has `title`, `description`, `address` and `employees`.
    #employees_of_company = serializers.SerializerMethodField()
    
    #def get_employees_of_company(self, obj):
        #temp = []
        #for i in EmployeeSerializer.id:
            #temp[i] = 
        #return temp
    
    #def to_representation(self, value):
     #   return "%s, %s" % value.last_name, value.first_name

    #employees_of_company = serializers.RelatedField(source='employee', read_only=True, many=True)
    employees_of_company = EmployeeSerializer(many=True)
    def create(self, validated):
        employee_data = validated.pop('employees_of_company')
    
        
        business=models.Business.objects.create(**validated)
        for employee in employee_data:
            models.Employee.objects.create(**employee, business=business)
        return business
    #def RelatedField.to_representation(self):

    class Meta:
        model = models.Business
        fields = ['title', 'description', 'address', 'id', 'employees_of_company']

