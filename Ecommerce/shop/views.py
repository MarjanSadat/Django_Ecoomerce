from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'index.html'


def products_view(request):
    all_products = Product.objects.all()
    context = {
        'all_products' : all_products
    }
    
    return render(request,'index.html',context)

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You Login successfully!'))
            return redirect('shop:products_view')
        else:
            messages.success(request,('Some Problem Happened !'))
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ('You Logged out successfully!'))
    return redirect('shop:products_view')
