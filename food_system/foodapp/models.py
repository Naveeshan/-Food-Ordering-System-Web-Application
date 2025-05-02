# from django.db import models
# from django import forms
# class User(models.Model):
#     name = models.CharField(max_length=255, verbose_name="Name")
#     age = models.PositiveIntegerField(verbose_name="Age")
#     email = models.EmailField(unique=True, verbose_name="Email")
#     contact = models.CharField(max_length=15, verbose_name="Contact Number")
#     password = models.CharField(max_length=255, verbose_name="Password") 


# class FoodOrder(models.Model):
#       customer_name = models.CharField(max_length=20)
#       food = models.CharField(max_length=100)
#       quantity = models.IntegerField()

# def __str__(self):
#     return f"{self.name} - {self.email}"
    
# from django.db import models

# class MenuItem(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=8, decimal_places=2)

#     def __str__(self):
#         return self.name

# class Order(models.Model):
#     customer_name = models.CharField(max_length=200)
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True)
#     quantity = models.PositiveIntegerField(default=1)
#     order_time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.customer_name} ordered {self.menu_item.name}"

# # foodapp/models.py

# from django.db import models

# class MenuItem(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     is_available = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name

# # foodapp/models.py (User model)

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     is_staff = models.BooleanField(default=False)  # For admin users

#     def __str__(self):
#         return self.name
# foodapp/models.py

from django.db import models

# User model
class User(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    age = models.PositiveIntegerField(verbose_name="Age")
    email = models.EmailField(unique=True, verbose_name="Email")
    contact = models.CharField(max_length=15, verbose_name="Contact Number")
    password = models.CharField(max_length=255, verbose_name="Password")
    is_staff = models.BooleanField(default=False)  # For admin users

    def __str__(self):
        return f"{self.name} - {self.email}"

# FoodOrder model
class FoodOrder(models.Model):
    customer_name = models.CharField(max_length=20)
    food = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order by {self.customer_name} for {self.food} x{self.quantity}"

# MenuItem model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="No description")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Order model
class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} ordered {self.menu_item.name} x{self.quantity}"
