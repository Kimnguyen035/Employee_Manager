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
    
    def validate_phone_number(self, value):
        list_phone = [
            '032','033','034','035','036','037','038','039',
            '070','076','077','078','079',
            '081','082','083','084','085',
            '056','058',
            '059'
        ]
        for item in value:
            if item[:3] not in list_phone or len(item) != 10:
                raise serializers.ValidationError(ERROR['phone_failed'])
        return value