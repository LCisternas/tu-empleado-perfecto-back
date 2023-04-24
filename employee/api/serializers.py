from rest_framework import serializers
from employee.models import Employee
from company.api.serializers import CompanySerializers

class EmployeeSerializer(serializers.ModelSerializer):
    company_data = CompanySerializers(source="category", read_only=True)
    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'rut', 'phone', 'company', 'company_data']