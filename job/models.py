from django.db import models

# Create your models here.
from django.db.models import Model


class Contact_Us(Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    title=models.CharField(max_length=50)
    message=models.CharField(max_length=300)
    def _str_(self):
        return self.email
