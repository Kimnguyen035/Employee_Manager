from rest_framework import serializers
from ..models.employee import Employee
from configs.variable_response import *

class IdGetEmployeeValidate(serializers.Serializer):
    id = serializers.IntegerField()
    birthday = serializers.DateTimeField(allow_null=True,required=False)
    
    def validate(self, value):
        queryset = Employee.objects.filter(id=value['id'])
        if not queryset.exists():
            raise serializers.ValidationError(ERROR['not_exists'])
        return value
    
class ListTelephoneValidate(serializers.Serializer):
    phone_number = serializers.ListField()
    