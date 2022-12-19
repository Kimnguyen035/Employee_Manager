from rest_framework import serializers
from ..models.telephone import Telephone
from configs.variable_response import *

class IdValidate(serializers.Serializer):
    id = serializers.IntegerField()
    
    def validate_id(self, value):
        queryset = Telephone.objects.filter(id=value)
        if not queryset.exists():
            raise serializers.ValidationError(ERROR['not_exists'])
        return value