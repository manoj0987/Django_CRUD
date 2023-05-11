from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Employees(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=220, unique=True)
    address = models.TextField()
    phone = models.IntegerField(unique=True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

    def __str__(self):
        return self.name