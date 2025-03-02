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