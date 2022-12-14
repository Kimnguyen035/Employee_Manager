from django.urls import path
from .views.employee_view import *

urlpatterns = [
    path('get-all', EmployeeView.as_view({'get':'get_all'})),
    path('get-detail/<int:id>', EmployeeView.as_view({'get':'get_detail'})),
    path('create-emloyee', EmployeeView.as_view({'post':'post'})),
]