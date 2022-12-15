from django.urls import path
from .views.employee_view import *
from .views.telephone_view import *

urlpatterns = [
    path('get-all', EmployeeView.as_view({'get':'get_all'})),
    path('get-detail/<int:id>', EmployeeView.as_view({'get':'get_detail'})),
    path('get-trash', EmployeeView.as_view({'get':'get_trash'})),
    
    path('create-emloyee', EmployeeView.as_view({'post':'create'})),
    
    path('edit-emloyee/<int:id>', EmployeeView.as_view({'put':'edit'})),
    
    path('delete-emloyee/<int:id>', EmployeeView.as_view({'delete':'delete'})),
    path('restore-emloyee/<int:id>', EmployeeView.as_view({'delete':'restore'})),
    path('drop-emloyee/<int:id>', EmployeeView.as_view({'delete':'drop'})),
    
    # telephone
    path('get-all-phone', TelephoneView.as_view({'get':'all_phone'})),
    path('create-phone', TelephoneView.as_view({'post':'create_phone'})),
]