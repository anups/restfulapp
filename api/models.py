from django.db import models

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    fax_number = models.CharField(max_length=50)


class Employee(models.Model):
    employee_ssn = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=50)
    contact_number = models.IntegerField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)