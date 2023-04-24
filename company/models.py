from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    direction = models.CharField(max_length=100, unique=True)
    rut = models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name