from .views import *

class TelephoneView(ViewSet):
    def all_phone(self, request):
        queryset = Telephone.objects.filter(deleted_at__isnull=True)
        serializer = TelephoneSerializer(queryset, many=True)
        return response_data(data=serializer.data)
    
    def detail_phone(self, request, pk):
        # test = Telephone.objects.get()
        return response_data()
    
    def create_phone(self, request):
        data = request.data.copy()
        post_save = TelephoneSerializer(data=data)
        if not post_save.is_valid(): 
            return validate_error(post_save.errors)
        post_save.save()
        return response_data(post_save.data)
    
    def edit_phone(self, request, id):
        data = request.data.copy()
        validate = IdValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        queryset = Telephone.objects.get(id=validate.data['id'])
        phone_save = TelephoneSerializer(queryset, data=data, partial=True)
        if not phone_save.is_valid():
            return validate_error(phone_save.errors, STATUS['FAIL_REQUEST'])
        phone_save.save()   
        return response_data(message=SUCCESS['update_phone'], data=phone_save.data)