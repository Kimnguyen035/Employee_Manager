from django.db import models
from .employee import Employee

class Telephone(models.Model):
    class Meta:
        db_table = 'telephone'
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, related_name='phone_number', on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()