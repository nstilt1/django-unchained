from rest_framework import serializers
from . import models

#class URLSerializer(serializers.HyperlinkedSerializer):
    #model = models.URL
    #fields = ['']

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Employee
        fields = ['first_name', 'last_name', 'email', 'id']

class BusinessEmployeeSerializer(serializers.ModelSerializer):
    #business_of_employee = BusinessSerializer()
    #employee_of_business = EmployeeSerializer()
    #employee_from_business = Employee.objects.select_related().get(id=id)


    employee_first_name = serializers.SerializerMethodField()
    employee_last_name = serializers.SerializerMethodField()

    def get_employee_last_name(self, obj):
        employee_last_name = getattr(obj.employee_of_business, 'last_name', None)
        return employee_last_name

    def get_employee_first_name(self, obj):
        employee_first_name = getattr(obj.employee_of_business, 'first_name', None)
        return employee_first_name

    class Meta:
        model = models.BusinessEmployee
        fields = ['employee_first_name', 'employee_last_name', 'business_of_employee','employee_of_business', 'is_owner', 'id']



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
    business_of_employee = BusinessEmployeeSerializer(many=True)
    def create(self, validated):
        employee_data = validated.pop('employees_of_business')
    
        business=models.Business.objects.create(**validated)
        for employee in employee_data:
            new_employee = models.Employee.objects.create(**employee)
            models.BusinessEmployee.objects.create(employee_of_business=new_employee, business_of_employee=business, is_owner=False)
        return business
    #def RelatedField.to_representation(self):

    class Meta:
        model = models.Business
        fields = ['title', 'description', 'address', 'id', 'business_of_employee']

