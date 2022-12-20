from .views import *

class TelephoneView(ViewSet):
    def all_phone(self, request):
        queryset = Telephone.objects.filter(deleted_at__isnull=True)
        serializer = TelephoneSerializer(queryset, many=True, not_fields=['created_at','updated_at','deleted_at'])
        return response_data(data=serializer.data)
    
    def detail_phone(self, request, id):
        validate = IdValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        queryset = Telephone.objects.get(id=validate.data['id'])
        if queryset.deleted_at is not None:
            return response_data(ERROR['not_exists_phone'],STATUS['NO_DATA'])
        phone = TelephoneSerializer(queryset)
        return response_data(data=phone.data)
    
    def add_phone(self, request):
        data = request.data.copy()
        post_save = TelephoneSerializer(data=data)
        if not post_save.is_valid():
            return validate_error(post_save.errors)
        post_save.save()
        return response_data(message=SUCCESS['create_phone'],data=post_save.data)
    
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
    
    def delete_phone(self, request, id):
        data = request.data.copy()
        validate = IdValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        delete_data = Telephone.objects.get(id=validate.data['id'])
        delete_data.deleted_at = datetime.now()
        delete_data.save()
        return response_data(message=SUCCESS['deleted_phone'],data={'id':delete_data.id})
    
    def get_trash(self, request):
        queryset = Telephone.objects.exclude(deleted_at__isnull=True)
        serializer = TelephoneSerializer(queryset, many=True)
        return response_data(data=serializer.data)
    
    def restore(self, request, id):
        data = request.data.copy()
        validate = IdValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        restore_data = Telephone.objects.get(id=validate.data['id'])
        restore_data.deleted_at = None
        restore_data.save()
        serializer = TelephoneSerializer(restore_data)
        return response_data(message=SUCCESS['restore_phone'], data=serializer.data)
    
    def drop_phone(self, request, id):
        data = request.GET.copy()
        validate = IdValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        Telephone.objects.get(id=validate.data['id']).delete()
        return response_data(message=SUCCESS['drop_phone'])