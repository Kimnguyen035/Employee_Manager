from rest_framework import serializers
from .action_seralizer import ActionSerializer
from ..models.employee_model import *
from configs.variable_response import *

class EmployeeSerializer(serializers.ModelSerializer, ActionSerializer):
    birthday = serializers.DateTimeField(allow_null=True,required=False)
    
    class Meta:
        model = Employee
        fields = ['id','name','birthday','created_at','updated_at','deleted_at']