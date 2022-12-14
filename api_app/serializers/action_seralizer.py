from rest_framework import serializers

class ActionSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(required=False, allow_null=True)
    updated_at = serializers.DateTimeField(required=False, allow_null=True)
    deleted_at = serializers.DateTimeField(required=False, allow_null=True)