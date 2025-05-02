from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from foodapp.models import User, FoodOrder
from foodapp.food import Inputform, LoginForm,FoodForm

def form(request):
    if request.method == 'POST':
        formdata = Inputform(request.POST)
        if formdata.is_valid():
            formdata.save()
            return redirect('login')
        else:
            return HttpResponse(f"Invalid values: {formdata.errors}")
    else:
        obj = Inputform()
        return render(request, 'reg.html', {'form': obj})

def login_view(request):
    if request.method == 'POST':  
        form = LoginForm(request.POST)  
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(name=name, password=password)
                request.session['user_id'] = user.id  
                return redirect('all_view')
            except User.DoesNotExist:
                messages.error(request, "Invalid username or password")  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def all_view(request):


    if request.method == 'POST':
        name = request.POST.get("name")
        food = request.POST.get("food")
        qty = request.POST.get("qty")

        if name and food and qty:
            FoodOrder.objects.create(customer_name = name,food=food, quantity=int(qty))
            messages.success(request, "Order submitted successfully!")
            return redirect('summary')  

    return render(request, 'all.html')

def order_summary(request):
    alldatas = FoodOrder.objects.all()
    return render(request, "summary.html", context={'alldatas': alldatas})

# # foodapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MenuItem, FoodOrder
from .food import Inputform, LoginForm, FoodForm
from django.contrib.auth.decorators import login_required

# Show menu to users
def menu_view(request):
    items = MenuItem.objects.all()  # Fetch all menu items
    return render(request, 'menu.html', {'items': items})

# Admin page to add new menu item
@login_required
def add_menu_item(request):
    if request.user.is_staff:  # Check if the user is admin
        if request.method == 'POST':
            form = FoodForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Menu item added successfully!")
                return redirect('menu')
        else:
            form = FoodForm()
        return render(request, 'add_menu_item.html', {'form': form})
    else:
        return redirect('menu')  # Redirect non-admin users to menu

# Admin page to update menu item
@login_required
def update_menu_item(request, item_id):
    if request.user.is_staff:  # Check if the user is admin
        item = get_object_or_404(MenuItem, id=item_id)
        if request.method == 'POST':
            form = FoodForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, "Menu item updated successfully!")
                return redirect('menu')
        else:
            form = FoodForm(instance=item)
        return render(request, 'update_menu_item.html', {'form': form})
    else:
        return redirect('menu')  # Redirect non-admin users to menu

# Admin page to delete menu item
@login_required
def delete_menu_item(request, item_id):
    if request.user.is_staff:  # Check if the user is admin
        item = get_object_or_404(MenuItem, id=item_id)
        item.delete()
        messages.success(request, "Menu item deleted successfully!")
        return redirect('menu')
    else:
        return redirect('menu')  # Redirect non-admin users to menu


# # Show menu to users
# def menu_view(request):
#     items = MenuItem.objects.all()
#     return render(request, 'menu.html', {'items': items})

# # Place an order
# def place_order(request, item_id):
#     item = get_object_or_404(MenuItem, id=item_id)
#     if request.method == 'POST':
#         customer_name = request.POST.get('customer_name')
#         quantity = request.POST.get('quantity')
#         if customer_name and quantity:
#             Order.objects.create(
#                 customer_name=customer_name,
#                 menu_item=item,
#                 quantity=quantity
#             )
#             return redirect('order_success')
#     return render(request, 'place_order.html', {'item': item})

# # After successful order
# def order_success(request):
#     return render(request, 'order_success.html')

# # Admin view to see all orders
# def view_orders(request):
#     orders = Order.objects.all().order_by('-order_time')
#     return render(request, 'view_orders.html', {'orders': orders})

# # Admin CRUD for Menu Items
# def add_menu_item(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         if name and price:
#             MenuItem.objects.create(name=name, price=price)
#             return redirect('menu_management')
#     return render(request, 'add_menu_item.html')

# def update_menu_item(request, item_id):
#     item = get_object_or_404(MenuItem, id=item_id)
#     if request.method == 'POST':
#         item.name = request.POST.get('name')
#         item.price = request.POST.get('price')
#         item.save()
#         return redirect('menu_management')
#     return render(request, 'update_menu_item.html', {'item': item})

# def delete_menu_item(request, item_id):
#     item = get_object_or_404(MenuItem, id=item_id)
#     item.delete()
#     return redirect('menu_management')

# def menu_management(request):
#     items = MenuItem.objects.all()
#     return render(request, 'menu_management.html', {'items': items})
