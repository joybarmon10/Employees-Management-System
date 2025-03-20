from django.db import models

# Create your models here.

# Name	Email	Address	Phone

class Employees(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    salary  = models.IntegerField()
    designation  = models.CharField(max_length=255)
    short_description = models.TextField()
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
