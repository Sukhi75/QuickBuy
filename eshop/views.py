from django.conf.urls import url
from django.shortcuts import redirect, render

from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from eshop.forms import ReviewForm
from .models import Category, Product, PostImage, PostColor, PostSize, ReviewRating
from cart.forms import CartAddProductForm

#list allthe products or filter products by a given category.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator=Paginator(products,12)
    page=request.GET.get('page')
    paged_products=paginator.get_page(page)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        paginator=Paginator(products,12)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
    return render(request,'index.html',
                                {'category':category,
                                'categories':categories,
                                'products':paged_products})

def all_product(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator=Paginator(products,12)
    page=request.GET.get('page')
    paged_products=paginator.get_page(page)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        paginator=Paginator(products,12)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
    return render(request,'our_products.html',
                                {'category':category,
                                'categories':categories,
                                'products':paged_products})




#retrieve and display a single product
def product_detail(request, id, slug, category_slug=None):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    photos = PostImage.objects.filter(product=product)
    category = None
    categories = Category.objects.all()
    color = PostColor.objects.filter(product=product)
    size = PostSize.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    reviews = ReviewRating.objects.filter(product=product)
    
    #description = PostImage.objects.filter(product=product)
    #title = PostImage.objects.filter(product=product)
    return render(request, 'detail.html',
                                  {'product':product,'photos':photos,'color':color,'size':size,'category':category,
                                'categories':categories, 'reviews':reviews, 'cart_product_form':cart_product_form })



def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(product_id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            return redirect(url)
            
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.name = form.cleaned_data['name']
                data.email = form.cleaned_data['email']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.save()
                return redirect(url)
                 
