from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from App1.forms import UserInfoForm, UserForm, ProductForm
from App1.models import UserInfo, Product, ProductReview, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import math


# Create your views here.
#Return Homepage of the products
def index (request):
    products = Product.objects.order_by('price')
    return render(request, 'APP1/index.html', {'products' :products})

def register (request):
    #Check if the form is submitted
    #registered = False
    Tryagain = False
    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        userinfo_form = UserInfoForm(data = request.POST)
        password = user_form['password'].value()
        confirm_password = user_form['confirm_password'].value()

        if user_form.is_valid() and userinfo_form.is_valid() and password == confirm_password:
            #Saving the new user
            user = user_form.save()
            #Hashing the password then save it
            user.set_password(user.password)
            user.save()

            #Save userinfo to database after ensuring that the data is stored to the same user
            userinfo = userinfo_form.save(commit = False)
            userinfo.user = user
            userinfo.save()
            #Put registered = true to change the view of the homepage for the registered users
            #registered = True
            return render(request, 'App1/login.html')
        else:
            #Tryagain allows making changes to the register.html page
            Tryagain = True
            user_form = UserForm()
            userinfo_form = UserInfoForm()
            return render(request, 'App1/register.html', {'user_form' : user_form,'userinfo_form' : userinfo_form, 'Tryagain' : Tryagain})

    #Send the form details to register.html file
    else:
        user_form = UserForm()
        userinfo_form = UserInfoForm()
        return render(request, 'App1/register.html', {'user_form' : user_form,'userinfo_form' : userinfo_form, 'Tryagain' : Tryagain })

#Login view
def user_login(request):
    WrongPassword = False #Variable used to display error message to the user if login failed
    sellerflag = False
    if request.method == 'POST':
        #Get the inputted data in login form
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Check the correctness of data
        user = authenticate(username=username, password=password)

        #If the data is correct
        if user:
            if user.is_active:

                login(request, user)
                current_user = UserInfo.objects.filter(user = request.user)
                if current_user[0].BuyerOrSeller == 'seller':
                    sellerflag = True
                return redirect('index')
                #return render(request, 'App1/index.html', {'sellerflag': sellerflag})
            else:
                WrongPassword = True
                return render(request, 'App1/login.html', {'WrongPassword': WrongPassword})
        else:
            WrongPassword = True
            return render(request, 'App1/login.html', {'WrongPassword': WrongPassword})

    #Send the form details to login.html file
    else:
        return render(request, 'App1/login.html', {'WrongPassword': WrongPassword})

#Logout view
@login_required      #This function isn't executed except if the user is logged in
def user_logout(request):
    logout(request)
    return redirect('index')


#Seller add products to be sold
@login_required
def add_product(request):
    product_error_flag = False
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit = False)
            product.seller = request.user
            if 'picture' in request.FILES:
                product.picture = request.FILES['picture']
            product.save()
            return render(request, 'App1/index.html', {'sellerflag': True})
        else:
            product_error_flag = True
            product_form = ProductForm()
            return render(request, 'App1/add_product.html', {'product_error_flag': product_error_flag, 'product_form': product_form})
    else:
        product_form = ProductForm()
        return render(request, 'App1/add_product.html', {'product_error_flag': product_error_flag, 'product_form': product_form})

#Product details page function
def product_details(request, id):
    #Required from John->pass to me the clicked product in main page as current_product
    current_product = Product.objects.filter(id = id)[0]
    average_rating=math.floor(current_product.get_average_rating())
    number_of_stars = [i for i in range(average_rating)]
    if(request.user.is_authenticated):
        current_user = UserInfo.objects.filter(user = request.user).first()    #changed it due to an indexerror
    else:
        current_user = "null"
    if request.method =="POST":
        rating = request.POST.get('rating', 3) #3 is the default value
        review_content = request.POST.get('content', '')
        review = ProductReview.objects.create(product = current_product, user = request.user, rating = rating, review_content = review_content)
        return render(request, 'App1/product_details.html', {'current_product':current_product,'number_of_stars':number_of_stars, 'current_user':current_user })
    else:
        return render(request, 'App1/product_details.html', {'current_product':current_product, 'number_of_stars':number_of_stars, 'current_user':current_user})

#Cart page function
@login_required
def cart_page(request):
    cart = CartItem.objects.filter(user = request.user, purchased = False)
    return render(request, 'App1/cart_page.html', {"cart":cart})


#Update Cart with items added only (what addtocart button does)
@login_required
def update_cart(request, id):
    if CartItem.objects.filter(user = request.user, item_id=id, purchased=False).exists():
        product = CartItem.objects.filter(user = request.user, item_id = id, purchased = False).first()
        product.quantity += 1
        product.total_item_price = product.quantity * product.item.price
    else:
        product = CartItem(user = request.user, item = Product.objects.filter(id = id).first(),
        total_item_price = Product.objects.filter(id = id).first().price )

    product.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
#Update Cart with items removed only (what remove button does)
@login_required
def remove_from_cart(request, id):
    cart = CartItem.objects.filter(user = request.user, purchased = False)
    item_to_be_removed = CartItem.objects.filter(user = request.user, id = id, purchased = False).first()
    item_to_be_removed.delete()
    return render(request, 'App1/cart_page.html', {"cart":cart})