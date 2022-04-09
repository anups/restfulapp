from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrganizationSerializer, EmployeeSerializer
from .models import Organization, Employee

# Create your views here.


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

