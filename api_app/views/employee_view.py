from .views import *

class EmployeeView(ViewSet):
    def get_all(self, request):
        queryset = Employee.objects.filter(deleted_at__isnull=True)
        serializer = EmployeeSerializer(queryset, many=True)
        return response_data(data=serializer.data)
    
    def get_data(self, id):
        validate = IdGetEmployeeValidate(data={'id':id})
        if not validate.is_valid():
            return False, validate.errors
        return True, validate.data['data']
    
    def get_detail(self, request, id):
        validate = IdGetEmployeeValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors)
        queryset = Employee.objects.get(id=validate.data['id'])
        serializer = EmployeeSerializer(queryset)
        return response_data(data=serializer.data)
    
    # def create(self, request):
    #     data = request.data.copy()
    #     post_save = EmployeeSerializer(data=data)
    #     if not post_save.is_valid():
    #         return validate_error(post_save.errors)
    #     data = post_save.data
    #     for item in post_save:
            
        
    #     post_save.save()
    #     return self.get_detail(request=request, id=post_save.data['id'])
    
    def create(self, request):
        data = request.data.copy()
        post_save = EmployeeSerializer(data=data)
        if not post_save.is_valid():
            return validate_error(post_save.errors)
        post_save.save()
        user_id = post_save.data['id']
        validate = ListTelephoneValidate(data=data)
        if not validate.is_valid():
            return validate_error(validate.errors)
        data =  validate.data.copy()
        list_phone = []
        for item in data['phone_number']:
            list_phone.append({
                'employee': user_id,
                'phone':item
            })
        data_save = TelephoneSerializer(data=list_phone, many=True)
        if not data_save.is_valid():
            return validate_error(data_save.errors)
        data_save.save()
        return self.get_detail(request=request, id=user_id)
    
    def edit(self, request, id):
        data = request.data.copy()
        validate = IdGetEmployeeValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        queryset = Employee.objects.get(id=validate.data['id'])
        data_save = EmployeeSerializer(queryset, data=data, partial=True)
        if not data_save.is_valid():
            return validate_error(data_save.errors, STATUS['FAIL_REQUEST'])
        data_save.save()
        return response_data(message=SUCCESS['update_employee'], data=data_save.data)
    
    def delete(self, request, id):
        data = request.data.copy()
        validate = IdGetEmployeeValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        delete_data = Employee.objects.get(id=validate.data['id'])
        # if delete_data.deleted_at is not None:
        #     return response_data(message=SUCCESS['not_exists_employee'], status=STATUS['NO_DATA'])
        delete_data.deleted_at = datetime.now()
        delete_data.save()
        return response_data(message=SUCCESS['deleted_employee'])
    
    def get_trash(self, request):
        queryset = Employee.objects.exclude(deleted_at__isnull=True)
        serializer = EmployeeSerializer(queryset, many=True)
        return response_data(data=serializer.data)
    
    def restore(self, request, id):
        data = request.data.copy()
        validate = IdGetEmployeeValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        restore_data = Employee.objects.get(id=validate.data['id'])
        # if restore_data.deleted_at is not None:
        #     return response_data(message=SUCCESS['not_exists_trash'], status=STATUS['NO_DATA'])
        restore_data.deleted_at = None
        restore_data.save()
        serializer = EmployeeSerializer(restore_data)
        return response_data(message=SUCCESS['restore_employee'], data=serializer.data)
    
    def drop(self, request, id):
        data = request.GET.copy()
        validate = IdGetEmployeeValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors,STATUS['NO_DATA'])
        Employee.objects.get(id=validate.data['id']).delete()
        return response_data(message=SUCCESS['drop_employee'])