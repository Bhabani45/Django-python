from django.db import models

# Create your models here.

class Employee(models.Model):
    Employee_ID= models.IntegerField()
    Employee_Name = models.CharField(max_length=10)
    Employee_Email = models.EmailField()
    class Meta:
        db_table = "Employee"



