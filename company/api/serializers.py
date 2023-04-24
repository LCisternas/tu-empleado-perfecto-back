from rest_framework import serializers
from company.models import Company

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'direction', 'rut', 'phone']