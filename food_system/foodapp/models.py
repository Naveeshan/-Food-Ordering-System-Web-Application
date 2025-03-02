from django.db import models
from django import forms
class User(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    age = models.PositiveIntegerField(verbose_name="Age")
    email = models.EmailField(unique=True, verbose_name="Email")
    contact = models.CharField(max_length=15, verbose_name="Contact Number")
    password = models.CharField(max_length=255, verbose_name="Password") 


class FoodOrder(models.Model):
      customer_name = models.CharField(max_length=20)
      food = models.CharField(max_length=100)
      quantity = models.IntegerField()

def __str__(self):
    return f"{self.name} - {self.email}"
    


