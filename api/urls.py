from django.urls import include, path
from rest_framework import routers
from .views import OrganizationViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
