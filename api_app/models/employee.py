from django.db import models

class Employee(models.Model):
    class Meta:
        db_table = 'employee'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()