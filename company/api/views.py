from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from company.models import Company
from company.api.serializers import CompanySerializers

class CompanyApiViewSet(ModelViewSet):
    serializer_class = CompanySerializers
    queryset = Company.objects.all()
    lookup_field = 'name'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']