from rest_framework import serializers
from ..models.employee import Employee
from configs.variable_response import *
from configs.variable_listphone import *

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
    
    def validate_phone_number(self, value):
        for item in value:
            if item[:3] not in LIST_PHONE_VN or len(item) != 10:
                raise serializers.ValidationError(ERROR['phone_failed'])
        return value