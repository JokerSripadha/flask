from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
class Role(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    salary=models.IntegerField()
    bonus=models.CharField(max_length=255)
    phone=models.IntegerField(max_length=255)
    hire_date=models.DateField()
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.firstname
    
