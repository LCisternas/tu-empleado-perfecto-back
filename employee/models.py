from django.db import models
from company.models import Company

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    rut = models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
