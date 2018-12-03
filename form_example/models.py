from django.db import models

# Create your models here.

class Collage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'college'


class Student(models.Model):
    name = models.CharField(max_length=30)
    fathername = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=12)
    address = models.CharField(max_length=500)