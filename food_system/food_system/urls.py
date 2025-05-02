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
from django.contrib import admin
from django.urls import path
from foodapp import views
# from foodapp.views import menu_view, place_order, order_success, view_orders, add_menu_item, update_menu_item, delete_menu_item, menu_management


app_name = 'foodapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.form, name='register'),
    path('login/', views.login_view, name='login'),
    path('all/', views.all_view, name='all_view'),
    
    path('summary/', views.order_summary, name='summary'),
    path('menu/', views.menu_view, name='menu'),  # Display menu
    path('add_menu/', views.add_menu_item, name='add_menu_item'),  # Admin can add menu item
    path('update_menu/<int:item_id>/', views.update_menu_item, name='update_menu_item'),  # Admin can update menu item
    path('delete_menu/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),  # Admin can delete menu item
    # path('order/<int:item_id>/', views.place_order, name='place_order'),
    # path('order_success/', views.order_success, name='order_success'),
    # path('orders/', views.view_orders, name='view_orders'),

    # # Admin-side management
    # path('admin/menu_management/', views.menu_management, name='menu_management'),
    # path('admin/add_menu_item/', views.add_menu_item, name='add_menu_item'),
    # path('admin/update_menu_item/<int:item_id>/', views.update_menu_item, name='update_menu_item'),
    # path('admin/delete_menu_item/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),

]

