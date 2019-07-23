from rest_framework import serializers
from . import models

class BusinessSerializer(serializers.ModelSerializer):
    #- the model itself has `title`, `description`, `address` and `employees`.
    class Meta:
        model = models.Business
        fields = ['title', 'description', 'address', 'employees']