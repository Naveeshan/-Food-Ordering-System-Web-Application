"""
URL configuration for food_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from foodapp import views
from foodapp.views import all_view,order_summary

app_name = 'foodapp'
urlpatterns = [
    path('register/', views.form, name='register'),
    path('login/', views.login_view, name='login'),
    # path('all/', views.all_view, name='all_view'),
    # path('summary/', views.order_summary, name='summary')
    path('all/', all_view, name='all_view'),
    path('summary/', order_summary, name='summary'),
]

