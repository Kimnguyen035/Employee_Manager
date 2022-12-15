from rest_framework import serializers
from .action_seralizer import ActionSerializer
from ..models.telephone import *
from configs.variable_response import *

class TelephoneSerializer(serializers.ModelSerializer, ActionSerializer):
    
    class Meta:
        model = Telephone
        fields = ['id','employee','phone','created_at','updated_at','deleted_at']