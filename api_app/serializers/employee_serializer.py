from rest_framework import serializers
from .action_seralizer import ActionSerializer
from ..models.employee import *
from configs.variable_response import *
from .telephone_serializer import *

class EmployeeSerializer(serializers.ModelSerializer, ActionSerializer):
    birthday = serializers.DateTimeField(allow_null=True,required=False)
    # phone_number = TelephoneSerializer(read_only=True,many=True)
    phone_number = serializers.SlugRelatedField(many=True,read_only=True,slug_field='phone')
    
    class Meta:
        model = Employee
        fields = ['id','name','birthday','phone_number','created_at','updated_at','deleted_at']