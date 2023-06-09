from django.urls import path
from .views.employee_view import *
from .views.telephone_view import *
from .views.excel_view import *

url_items = {
    'url_employee': [
        path('get-all', EmployeeView.as_view({'get':'get_all'})),
        path('get-detail/<int:id>', EmployeeView.as_view({'get':'get_detail'})),
        path('get-trash-employee', EmployeeView.as_view({'get':'get_trash'})),
        
        path('create-emloyee', EmployeeView.as_view({'post':'create'})),
        
        path('edit-emloyee/<int:id>', EmployeeView.as_view({'put':'edit'})),
        
        path('delete-emloyee/<int:id>', EmployeeView.as_view({'delete':'delete'})),
        path('restore-emloyee/<int:id>', EmployeeView.as_view({'delete':'restore'})),
        path('drop-emloyee/<int:id>', EmployeeView.as_view({'delete':'drop'})),
    ],
    'url_phone': [
        path('get-all-phone', TelephoneView.as_view({'get':'all_phone'})),
        path('detail-phone/<int:id>', TelephoneView.as_view({'get':'detail_phone'})),
        path('get-trash-phone', TelephoneView.as_view({'get':'get_trash'})),
        path('add-phone', TelephoneView.as_view({'post':'add_phone'})),
        path('edit-phone/<int:id>', TelephoneView.as_view({'put':'edit_phone'})),
        path('delete-phone/<int:id>', TelephoneView.as_view({'delete':'delete_phone'})),
        path('restore-phone/<int:id>', TelephoneView.as_view({'delete':'restore'})),
        path('drop-phone/<int:id>', TelephoneView.as_view({'delete':'drop_phone'})),
    ],
    'url_phone': [
        path('excel-convert-json', ExcelView.as_view({'get':'excel_convert_json'})),
    ]
}

urlpatterns = []

for item in url_items:
    urlpatterns += url_items[item]