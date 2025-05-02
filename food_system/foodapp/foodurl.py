from django.urls import path
from foodapp import views

app_name = 'foodapp'
urlpatterns = [
    path('register/', views.form, name='register'),
    path('login/', views.login_view, name='login'),
    path('all/', views.all_view, name='all_view'),
    
    path('summary/', views.order_summary, name='summary'),
    path('menu/', views.menu_view, name='menu'),
    # path('order/<int:item_id>/', views.place_order, name='place_order'),
    # path('order_success/', views.order_success, name='order_success'),
    # path('orders/', views.view_orders, name='view_orders'),

    # # Admin-side management
    # path('admin/menu_management/', views.menu_management, name='menu_management'),
    # path('admin/add_menu_item/', views.add_menu_item, name='add_menu_item'),
    # path('admin/update_menu_item/<int:item_id>/', views.update_menu_item, name='update_menu_item'),
    # path('admin/delete_menu_item/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),
    
]