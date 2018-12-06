from django.shortcuts import render,get_object_or_404, redirect
from .models import Product
from .forms import ReviewForm



def view_products(request):
    products=Product.objects.all()
    return render(request, "products/index.html", {"products":products})

def product_detail(request, id):
    product=get_object_or_404(Product, id=id)
    form = ReviewForm()
    return render(request, "products/product_detail.html",{"product":product, "form":form})
    
    
def add_review(request, id):
    review = ReviewForm(request.POST)
    product = get_object_or_404(Product, id=id)
    review.product = product
    review.save()
    return redirect('product_detail', id=product.id)

    
