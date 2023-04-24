from rest_framework.routers import DefaultRouter
from employee.api.views import EmployeeApiViewSet

router_employee = DefaultRouter()
router_employee.register(prefix='employee', basename='employee', viewset=EmployeeApiViewSet)