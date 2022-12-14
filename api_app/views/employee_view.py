from rest_framework.viewsets import ViewSet
from helpers.response import *
from ..serializers.employee_serializer import *
from ..validations.employee_validate import *
from datetime import datetime

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
        status, data = self.get_data(id)
        if status:
            return response_data(data)
        return response_data(message=ERROR['not_exists_employee'])
    
    def create(self, request):
        data = request.data.copy()
        post_save = EmployeeSerializer(data=data)
        if not post_save.is_valid():
            return validate_error(post_save.errors)
        post_save.save()
        return response_data(message=SUCCESS['create_employee'], data=post_save.data)
    
    def edit(self, request, id):
        data = request.data.copy()
        status, data_id = self.get_data(id)
        if not status:
            return response_data(message=ERROR['not_exists_employee'],status=STATUS['NO_DATA'])
        queryset = Employee.objects.get(id=data_id['id'])
        data_save = EmployeeSerializer(queryset, data=data, partial=True)
        if not data_save.is_valid():
            return validate_error(data_save.errors, STATUS['FAIL_REQUEST'])
        data_save.save()
        return response_data(message=SUCCESS['update_employee'], data=data_save.data)
    
    def delete(self, request, id):
        data = request.data.copy()
        status, data_id = self.get_data(id)
        if not status or data_id['deleted_at'] is not None:
            return response_data(message=ERROR['not_exists_employee'],status=STATUS['NO_DATA'])
        delete_data = Employee.objects.get(id=data_id['id'])
        delete_data.deleted_at = datetime.now()
        delete_data.save()
        return response_data(message=SUCCESS['deleted_employee'])
    
    def get_trash(self, request):
        queryset = Employee.objects.exclude(deleted_at__isnull=True)
        serializer = EmployeeSerializer(queryset, many=True)
        return response_data(data=serializer.data)
    
    def restore(self, request, id):
        data = request.data.copy()
        status, data_id = self.get_data(id)
        if not status or data_id['deleted_at'] is None:
            return response_data(message=ERROR['not_exists_trash'],status=STATUS['NO_DATA'])
        restore_data = Employee.objects.get(id=data_id['id'])
        restore_data.deleted_at = None
        restore_data.save()
        return response_data(message=SUCCESS['restore_employee'])
    
    def drop(self, request, id):
        data = request.GET.copy()
        status, data_id = self.get_data(id)
        if not status:
            return response_data(message=ERROR['not_exists_post'],status=STATUS['NO_DATA'])
        Employee.objects.get(id=data_id['id']).delete()
        return response_data(message=SUCCESS['drop_employee'])