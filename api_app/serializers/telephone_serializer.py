from rest_framework import serializers
from .action_seralizer import ActionSerializer
from ..models.telephone import *
from configs.variable_response import *

class TelephoneSerializer(serializers.ModelSerializer, ActionSerializer):
    phone = serializers.CharField()
    
    # ============================= function contructor =======================
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        not_fields = kwargs.pop('not_fields', None)
        super().__init__(*args, **kwargs)
        list_key = list(self.get_fields().keys())
        if fields is not None:
            # if not set(fields).issubset(list_key):
            #     raise serializers.ValidationError('fails')
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        if not_fields is not None:
            # if not set(not_fields).issubset(list_key):
            #     raise serializers.ValidationError('fails')
            for item in not_fields:
                self.fields.pop(item)
    # ============================== end contructor ===========================
    
    class Meta:
        model = Telephone
        fields = ['id','employee','phone','created_at','updated_at','deleted_at']