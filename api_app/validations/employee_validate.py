from rest_framework import serializers
from ..models.employee_model import Employee
from configs.variable_response import *
from ..serializers.employee_serializer import *

class IdGetEmployeeValidate(serializers.Serializer):
    id = serializers.IntegerField()
    
    data = EmployeeSerializer(required=False, allow_null=False)
    
    def validate(self, value):
        queryset = Employee.objects.filter(id=value['id'])
        if not queryset.exists():
            raise serializers.ValidationError(ERROR['not_exists'])
        value['data'] = queryset.values()[0]
        return value