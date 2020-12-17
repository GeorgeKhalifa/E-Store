from django.shortcuts import render
from product_app.forms import ProductForm
from product_app.models import Product
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request,'product_app/index.html')

def fill_product_form(request):
    product_form = ProductForm()

    if request.method == 'POST':
        product_form = ProductForm(data=request.POST)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.product_picture = request.FILES['product_picture']
            product.save()
            product=ProductForm()
            print("DONE!")
        else:
            print("ERROR!")

    return render(request,'product_app/fill_product.html',{'product_form':product_form})


def details_product(request,id):
    product_details= Product.objects.get(pk=id)
    return render(request,'product_app/detail.html',{'product_details':product_details})

def printproducts(request):
    product_list = Product.objects.all()
    product_dict={'products':product_list}
    return render(request,'product_app/product_list.html',context=product_dict)