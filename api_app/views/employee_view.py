from rest_framework.viewsets import ViewSet
from helpers.response import *
from ..serializers.employee_serializer import *
from ..validations.employee_validate import *

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
    
    def post(self, request):
        data = request.data.copy()
        post_save = EmployeeSerializer(data=data)
        if not post_save.is_valid():
            return validate_error(post_save.errors)
        post_save.save()
        return response_data(message=SUCCESS['create_employee'], data=post_save.data)