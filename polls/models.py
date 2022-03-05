from django.db import models

class person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.IntegerField()
    regno=models.CharField(max_length=20)

class Details(models.Model):
    Shirt_Size=(
        ('S','Small'),
        ('M', 'Medium'),
        ('L','Large'),
    )
    name=models.CharField(max_length=40)
    shirt_size=models.CharField(max_length=1,choices=Shirt_Size)
