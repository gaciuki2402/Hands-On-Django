from django.db import models

# Create your models here.


class Leads(models.Model):
    username=models.CharField(max_length=156,unique=True)
    email=models.EmailField(max_length=157,unique=True)
    active=models.BooleanField(default=False)
    full_name=models.CharField(max_length=256)
    phone=models.CharField(max_length=15,unique=True)
    town=models.CharField(max_length=57)


    def __str__(self):
        return f"{self.username}- {self.email}"

    class Meta:
        verbose_name_plural="Leads"