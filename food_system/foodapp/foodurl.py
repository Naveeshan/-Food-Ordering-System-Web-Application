from django.urls import path
from foodapp import views

app_name = 'foodapp'
urlpatterns = [
    path('register/', views.form, name='register'),
    path('login/', views.login_view, name='login'),
    path('all/', views.all_view, name='all_view'),
    path('summary/', views.order_summary, name='summary')

]