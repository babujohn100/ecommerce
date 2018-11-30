from django.shortcuts import render,get_object_or_404
from .models import Product



def view_products(request):
    products=Product.objects.all()
    return render(request, "products/index.html", {"products":products})

def product_detail(request, id):
    product=get_object_or_404(Product, id=id)
    return render(request, "products/product_detail.html",{"product":product})
    
