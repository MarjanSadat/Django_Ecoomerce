from django.shortcuts import render, redirect
from .models import Product, Category
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'index.html'

def category_summary(request):
    all_cat = Category.objects.all()
    context = {
        'cats':all_cat,
    }    
    return render(request,'category_summary.html', context)


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

def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product' : product
    }
    print('**'*10)
    return render(request, 'product.html', context)

def category(request, cat):
    # cat = cat.replace('-',' ')
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        context = {
            'products' : products,
            'category' : category,
        }
        return render(request, 'category.html', context)

    except:        
        messages.success(request, ('This Category is Empty!'))
        return redirect('shop:products_view')
