import uuid
from django.db import models

# Create your models here.
class ITSP(models.Model):
    Team=models.CharField(max_length=45)
    memeber1=models.CharField(max_length=100)
    memeber2=models.CharField(max_length=100)
    email1=models.EmailField(max_length=100)
    email2=models.EmailField(max_length=100)
    Topic=models.CharField(max_length=100)
    desc=models.CharField(max_length=250)
    date=models.DateField()

    def __str__(self):
        return self.Team
    