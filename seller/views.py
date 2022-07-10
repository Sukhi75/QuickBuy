from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileEditForm
from django.shortcuts import render, redirect
from .models import Seller, Profile
from eshop.models import Product
from .forms import ProductForm
from django.utils.text import slugify
def become_seller(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')  

    else:
        form = UserRegisterForm()
    return render(request, 'become_seller.html',{'form':form})




@login_required
def seller_dashboard(request):
    seller = request.user.seller
    products = seller.products.all()
    return render(request, 'seller_dashboard.html',{'seller':seller, 'products':products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.seller
            product.slug = slugify(product.name)
            product.save()

            return redirect('seller_dashboard')

    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form':form})


@login_required
def edit(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.seller.profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()

    else:
        profile_form = ProfileEditForm(instance=request.user.seller.profile)

    return render(request, 'profile_edit.html', {'profile_form':profile_form})
