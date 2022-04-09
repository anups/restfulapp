from rest_framework import serializers
from .models import Organization, Employee


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('name', 'address', 'fax_number',)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_ssn', 'employee_name', 'contact_number',)
