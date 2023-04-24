from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from employee.models import Employee
from employee.api.serializers import EmployeeSerializer

class EmployeeApiViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company__name']