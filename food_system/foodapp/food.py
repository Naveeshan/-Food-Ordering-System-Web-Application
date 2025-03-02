from django import forms
from foodapp.models import User,FoodOrder

class Inputform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'email', 'contact', 'password']
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodOrder
        fields = ['customer_name','food', 'quantity']