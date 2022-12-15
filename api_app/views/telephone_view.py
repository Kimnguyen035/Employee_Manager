# ========== include rest_framework ==========
from rest_framework.viewsets import ViewSet
# =============== end include  ===============
from helpers.response import *
from ..serializers.telephone_serializer import *

class TelephoneView(ViewSet):
    def all_phone(self, request):
        queryset = Telephone.objects.filter(deleted_at__isnull=True)
        serializer = TelephoneSerializer(queryset, many=True)
        return response_data(data=serializer.data)
    
    def create_phone(self, request):
        data = request.data.copy()
        post_save = TelephoneSerializer(data=data)
        if not post_save.is_valid(): 
            return validate_error(post_save.errors)
        post_save.save()
        return response_data(post_save.data)