from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from App1.forms import UserInfoForm, UserForm, ProductForm, OrderForm,StatusForm
from App1.models import UserInfo, Product, ProductReview, CartItem,Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
import math
from decimal import Decimal
import datetime

# Create your views here.
#Return Homepage of the products
class Controller():
    def index_c (self, request):
         search_query=request.GET.get('search', '')
         search_query2=request.GET.get('search2', '')
         total_number=0
         if(request.user.is_authenticated):
             cart = CartItem.objects.filter(user = request.user, purchased = False)
             total_number=0
             for product in cart:
                total_number += product.quantity
         if search_query:
             products=Product.objects.all().filter(name__icontains=search_query).exclude(in_stock = 0)
         elif search_query2:
             products=Product.objects.all().filter(secondary_category__icontains=search_query2).exclude(in_stock = 0)
         else:
             products = Product.objects.all().exclude(in_stock = 0)
         return render(request, 'APP1/index.html', {'products' :products,'total_number':total_number})

    def index_sort_price_c (self, request):
         products = Product.objects.order_by('price').exclude(in_stock = 0)
         total_number=0
         if(request.user.is_authenticated):
             cart = CartItem.objects.filter(user = request.user, purchased = False)
             total_number=0
             for product in cart:
                total_number += product.quantity
         return render(request, 'APP1/index.html', {'products' :products,'total_number':total_number})

    def index_sort_newest_c (self, request):
         products = Product.objects.order_by('id').reverse().exclude(in_stock = 0)
         total_number=0
         if(request.user.is_authenticated):
             cart = CartItem.objects.filter(user = request.user, purchased = False)
             total_number=0
             for product in cart:
                total_number += product.quantity
         return render(request, 'APP1/index.html', {'products' :products,'total_number':total_number})

    def index_sort_rating_c (self, request):
         products=sorted(Product.objects.all().exclude(in_stock = 0),key=lambda x:x.get_average_rating(),reverse=True)
         total_number=0
         if(request.user.is_authenticated):
             cart = CartItem.objects.filter(user = request.user, purchased = False)
             total_number=0
             for product in cart:
                total_number += product.quantity
         return render(request, 'APP1/index.html', {'products' :products,'total_number':total_number})

    def index_category_c (self, request):
         products = Product.objects.all().filter(main_category='men').exclude(in_stock = 0)
         total_number=0
         if(request.user.is_authenticated):
             cart = CartItem.objects.filter(user = request.user, purchased = False)
             total_number=0
             for product in cart:
                total_number += product.quantity
         return render(request, 'APP1/index.html', {'products' :products,'total_number':total_number})

    def index_category1_c (self, request):
         products = Product.objects.all().filter(main_category='women').exclude(in_stock = 0)
         total_number=0
         if(request.user.is_authenticated):
             cart = CartItem.objects.filter(user = request.user, purchased = False)
             total_number=0
             for product in cart:
                total_number += product.quantity
         return render(request, 'APP1/index.html', {'products' :products,'total_number':total_number})

    def index_category2_c (self, request):
         products = Product.objects.all().filter(main_category='kids').exclude(in_stock = 0)
         total_number=0
         if(request.user.is_authenticated):
             cart = CartItem.objects.filter(user = request.user, purchased = False)
             total_number=0
             for product in cart:
                total_number += product.quantity
         return render(request, 'APP1/index.html', {'products' :products,'total_number':total_number})

    def index_category3_c (self, request):
         products = Product.objects.all().filter(secondary_category='top').exclude(in_stock = 0)
         total_number=0
         if(request.user.is_authenticated):
             cart = CartItem.objects.filter(user = request.user, purchased = False)
             total_number=0
             for product in cart:
                total_number += product.quantity
         return render(request, 'APP1/index.html', {'products' :products,'total_number':total_number})

    def index_category4_c (self, request):
         products=Product.objects.all().filter(secondary_category='bottom').exclude(in_stock = 0)
         total_number=0
         if(request.user.is_authenticated):
             cart = CartItem.objects.filter(user = request.user, purchased = False)
             total_number=0
             for product in cart:
                total_number += product.quantity
         return render(request, 'APP1/index.html', {'products':products,'total_number':total_number})

    def index_category5_c (self, request):
         products=Product.objects.all().filter(secondary_category='coats_jackets').exclude(in_stock = 0)
         total_number=0
         if(request.user.is_authenticated):
             cart = CartItem.objects.filter(user = request.user, purchased = False)
             total_number=0
             for product in cart:
                total_number += product.quantity
         return render(request, 'APP1/index.html', {'products':products,'total_number':total_number})

    def register_c (self, request):
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
    def user_login_c(self, request):
        WrongPassword = False #Variable used to display error message to the user if login failed
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
                    return redirect('index')
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

    def user_logout_c(self, request):
        logout(request)
        return redirect('index')


    #Seller add products to be sold

    def add_product_c(self, request):
        product_error_flag = False
        if request.method == "POST":
            product_form = ProductForm(request.POST, request.FILES)
            if product_form.is_valid():
                product = product_form.save(commit = False)
                product.seller = request.user
                if 'picture' in request.FILES:
                    product.picture = request.FILES['picture']
                product.save()
                return render(request, 'App1/confirm_product_form.html')
            else:
                product_error_flag = True
                product_form = ProductForm()
                return render(request, 'App1/add_product.html', {'product_error_flag': product_error_flag, 'product_form': product_form})
        else:
            product_form = ProductForm()
            return render(request, 'App1/add_product.html', {'product_error_flag': product_error_flag, 'product_form': product_form})

    #Product details page function
    def product_details_c(self, request, id):
        #Required from John->pass to me the clicked product in main page as current_product
        products = Product.objects.all().exclude(in_stock = 0)
        current_product = Product.objects.filter(id = id)[0]
        average_rating=math.floor(current_product.get_average_rating())
        number_of_stars = [i for i in range(average_rating)]
        ##for recommendations

        if(request.user.is_authenticated):
             current_product.views.add(request.user)
        total_number=0
        if(request.user.is_authenticated):
            current_user = UserInfo.objects.filter(user = request.user).first()    #changed it due to an indexerror
            cart = CartItem.objects.filter(user = request.user, purchased = False)
            total_number=0
            for product in cart:
                total_number += product.quantity
        else:
            current_user = "null"
        if request.method =="POST":
            rating = request.POST.get('rating', 0)
            review_content = request.POST.get('content', '')
            review = ProductReview.objects.create(product = current_product, user = request.user, rating = rating, review_content = review_content)
            average_rating=math.floor(current_product.get_average_rating())
            number_of_stars = [i for i in range(average_rating)]
            return render(request, 'App1/product_details.html', {'current_product':current_product,'number_of_stars':number_of_stars, 'current_user':current_user,'products':products,'total_number':total_number})
        else:
            return render(request, 'App1/product_details.html', {'current_product':current_product, 'number_of_stars':number_of_stars, 'current_user':current_user,'products':products,'total_number':total_number})


    def favourite_list_c(self, request):
        new = Product.objects.filter(favourites=request.user).exclude(in_stock = 0)
        cart = CartItem.objects.filter(user = request.user, purchased = False)
        total_number=0
        for product in cart:
            total_number += product.quantity
        return render(request,'App1/favourites.html',{'new':new,'total_number':total_number})


    def favourite_add_c(self, request,id):
        product= get_object_or_404(Product,id=id)
        if product.favourites.filter(id=request.user.id).exists():
            product.favourites.remove(request.user)
        else:
            product.favourites.add(request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])



    def cart_page_c(self, request):
        cart = CartItem.objects.filter(user = request.user, purchased = False)
        total_cost=0
        total_number=0
        for product in cart:
            if(product.item.currency == 'L.E'):
                total_item_price = product.total_item_price / 15.7
            elif (product.item.currency == '€'):
                total_item_price = product.total_item_price / 0.82
            else:
                total_item_price = product.total_item_price
            if (product.item.in_stock < product.quantity):
                product.quantity = product.item.in_stock
                if(product.item.in_stock == 0):
                    product.delete()
                else:
                    product.save()
            total_cost += total_item_price
            total_number += product.quantity

        return render(request, 'App1/cart_page.html', {"cart":cart,"total_cost":round(total_cost,2),"total_number":total_number})



    def update_cart_c(self, request, id):
        if CartItem.objects.filter(user = request.user, item_id=id, purchased=False).exists():
            if CartItem.objects.filter(user = request.user, item_id = id, purchased = False).first().quantity < Product.objects.filter(id = id).first().in_stock:
                product = CartItem.objects.filter(user = request.user, item_id = id, purchased = False).first()
                product.quantity += 1
                product.total_item_price = product.quantity * product.item.price
                product.save()
        else:
            product = CartItem(user = request.user, item = Product.objects.filter(id = id).first(),
            total_item_price = Product.objects.filter(id = id).first().price )
            product.save()

        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    def update_cart2_c(self, request, id):
        product = CartItem.objects.filter(user = request.user, item_id = id, purchased = False).first()
        if product.quantity > 1:
            product.quantity -= 1
            product.total_item_price = product.quantity * product.item.price
            product.save()
        elif product.quantity == 1:
            product.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


    #Update Cart with items removed only (what remove button does)

    def remove_from_cart_c(self, request, id):
        cart = CartItem.objects.filter(user = request.user, purchased = False)
        item_to_be_removed = CartItem.objects.filter(user = request.user, id = id, purchased = False).first()
        item_to_be_removed.delete()
        return redirect ('App1:cart')
        

    #Checkout view

    def checkout_c(self, request):
        checkout_form = OrderForm()
        user_info = UserInfo.objects.filter(user = request.user)[0]
        products = CartItem.objects.filter(user = request.user, purchased=False)
        total_cost = 0
        new_total_cost = 0
        points = user_info.get_offer_points()

        for product in products:
            if (product.item.currency == 'L.E'):
                total_item_price = product.total_item_price / 15.7

            elif (product.item.currency == '€'):
                total_item_price = product.total_item_price / 0.82
            else:
                total_item_price = product.total_item_price

            total_cost += total_item_price

        if request.method == 'POST':
            checkout_form = OrderForm(request.POST)
            if checkout_form.is_valid():
                order = checkout_form.save(commit = False)
                currency = request.POST.get("currency")
                payment_method = request.POST.get("payment_method")
                discount_points = request.POST.get('discount_points')
                order.currency = currency
                order.method_of_payment = payment_method

                if (discount_points == 'yes'):
                    if (points == 0):
                        new_total_cost = total_cost
                        points = points+int(total_cost/10)
                    elif (points >= 100):
                        new_total_cost = 0
                        points = points - 100
                    else:
                        new_total_cost = total_cost*((100-points)/100)
                        points = 0
                elif (discount_points == 'no'):
                    new_total_cost = total_cost
                    points = points+int(total_cost/10)



                if (currency == 'L.E'):
                    new_total_cost *= 15.7
                elif (currency == '€'):
                    new_total_cost *= 0.82
                    #Updated
                order.total_cost = round(total_cost, 2)
                order.new_total_cost = round(new_total_cost, 2)
                order.user = request.user
                order.save()


                if (payment_method == 'credit'):
                    return render(request, 'App1/checkout2.html', {'new_total_cost': round(new_total_cost, 2), 'currency': currency, 'points': points})
                elif (payment_method == 'cod'):
                    return render(request, 'App1/checkout3.html', {'new_total_cost': round(new_total_cost, 2), 'currency': currency, 'points': points})

            else:
                return render(request, 'App1/checkout.html', {'checkout_form': checkout_form, 'total_cost': round(total_cost,2), 'points': points})
        else:
            return render(request, 'App1/checkout.html', {'checkout_form': checkout_form, 'total_cost': round(total_cost,2), 'points': points})

    #Confirm payment view

    def confirm_c(self, request, points):
        order = Order.objects.filter(user = request.user).last()
        items = CartItem.objects.filter(user = request.user, purchased=False)
        user_info = UserInfo.objects.filter(user = request.user)[0]
        user_info.set_offer_points(points)
        user_info.save()
        for product in items:
            product.purchased = True
            product.item.in_stock = product.item.in_stock-product.quantity
            product.in_order = order
            product.save()
            Product.objects.filter(id = product.item.id).update(in_stock = product.item.in_stock)
            Product.objects.filter(id = product.item.id).first().save()
        order.purchase_date = datetime.datetime.now()
        order.save()
        return render(request, 'App1/confirm_payment.html')

    def product_status_c(self, request):
        Products=Product.objects.filter(seller=request.user)
        return render(request,'App1/product_status.html',{'editupdate':Products})


    def edit_product_c(self, request,id):
        displayprod=Product.objects.get(id=id)
        return render(request,'App1/edit_product.html',{'editupdate':displayprod})



    def update_product_c(self, request,id):
        updateprod=Product.objects.get(id=id)
        product_form=StatusForm(request.POST,instance=updateprod)
        if product_form.is_valid():
            product_form.save()
            return redirect ('App1:product_status')


        return render(request, 'App1/edit_product.html', {'editupdate':updateprod})


    def remove_product_c(self, request, id):
        Removed_Product= Product.objects.get(id=id)
        Removed_Product.delete()
        return redirect ("App1:product_status")


    def history_c(self, request):
        orders = Order.objects.filter(user = request.user).exclude(purchase_date = None).order_by('-purchase_date')
        return render(request, 'App1/history.html', {"orders": orders})

    def recommendation_logic_c(self, request):
        #men women kids
        #top bottom coats/jackets
        recommended_products=Product.objects.all().exclude(in_stock = 0)
        if(request.user.is_authenticated):
            filtered_views = Product.objects.filter(views=request.user).exclude(in_stock = 0)
            #count main_category
            men_count = filtered_views.filter(main_category='men').count()
            women_count = filtered_views.filter(main_category='women').count()
            kids_count = filtered_views.filter(main_category='kids').count()
            #count second_category
            top_count = filtered_views.filter(secondary_category='top').count()
            bottom_count =  filtered_views.filter(secondary_category='bottom').count()
            coats_jackets_count = filtered_views.filter(secondary_category='coats_jackets').count()

            if (men_count > women_count and men_count > kids_count): # MEN

                if (top_count> bottom_count and top_count > coats_jackets_count):  #MEN & TOP
                    recommended_products = Product.objects.filter(main_category='men',secondary_category='top').exclude(in_stock =0)
                elif(bottom_count > top_count and bottom_count > coats_jackets_count): #MEN & BOTTOM
                    recommended_products = Product.objects.filter(main_category='men',secondary_category='bottom').exclude(in_stock =0)
                else: #MEN &JACKETS/COATS
                    recommended_products = Product.objects.filter(main_category='men',secondary_category='coats_jackets').exclude(in_stock =0)

            elif (women_count> men_count and women_count> kids_count): #WOMEN
                if (top_count> bottom_count and top_count > coats_jackets_count):  #WOMEN & TOP
                    recommended_products = Product.objects.filter(main_category='women',secondary_category='top').exclude(in_stock =0)
                elif (bottom_count > top_count and bottom_count > coats_jackets_count): #WOMEN & BOTTOM
                    recommended_products = Product.objects.filter(main_category='women',secondary_category='bottom').exclude(in_stock =0)
                else: #WOMEN &JACKETS/COATS
                    recommended_products = Product.objects.filter(main_category='women',secondary_category='coats_jackets').exclude(in_stock =0)

            elif(kids_count> men_count and kids_count> women_count): #KIDS
                if (top_count > bottom_count and top_count > coats_jackets_count):  #KIDS & TOP
                    recommended_products = Product.objects.filter(main_category='kids',secondary_category='top').exclude(in_stock =0)

                elif (bottom_count > top_count and bottom_count > coats_jackets_count): #KIDS & BOTTOM
                    recommended_products = Product.objects.filter(main_category='kids',secondary_category='bottom').exclude(in_stock =0)
                else: #KIDS &JACKETS/COATS
                    recommended_products = Product.objects.filter(main_category='kids',secondary_category='coats_jackets').exclude(in_stock =0)
        else:
            recommended_products=Product.objects.all().exclude(in_stock =0)

        search_query=request.GET.get('search', '')
        search_query2=request.GET.get('search2', '')
        total_number=0
        if(request.user.is_authenticated):
             cart = CartItem.objects.filter(user = request.user, purchased = False)
             total_number=0
             for product in cart:
                total_number += product.quantity
        if search_query:
             products=Product.objects.all().filter(name__icontains=search_query).exclude(in_stock =0)
        elif search_query2:
             products=Product.objects.all().filter(secondary_category__icontains=search_query2).exclude(in_stock =0)
        else:
             products = Product.objects.all().exclude(in_stock =0)
        return render(request,'App1/index.html',{'products':products,'recommended_products':recommended_products,'total_number':total_number})










C = Controller()



def index (request):
    result = C.index_c(request)
    return result

def index_sort_price (request):
    result = C.index_sort_price_c(request)
    return result
def index_sort_newest (request):
    result = C.index_sort_newest_c(request)
    return result

def index_sort_rating (request):
    result = C.index_sort_rating_c(request)
    return result

def index_category (request):
    result = C.index_category_c(request)
    return result

def index_category1 (request):
    result = C.index_category1_c(request)
    return result

def index_category2 (request):
    result = C.index_category2_c(request)
    return result

def index_category3 (request):
    result = C.index_category3_c(request)
    return result

def index_category4 (request):
    result = C.index_category4_c(request)
    return result

def index_category5 (request):
    result = C.index_category5_c(request)
    return result

def register (request):
    result = C.register_c(request)
    return result
#Login view
def user_login(request):
    result = C.user_login_c(request)
    return result
#Logout view
@login_required      #This function isn't executed except if the user is logged in
def user_logout(request):
    result = C.user_logout_c(request)
    return result


#Seller add products to be sold
@login_required
def add_product(request):
    result = C.add_product_c(request)
    return result

#Product details page function
def product_details(request, id):
    result = C.product_details_c(request, id)
    return result

@login_required
def favourite_list(request):
    result = C.favourite_list_c(request)
    return result

@login_required
def favourite_add(request,id):
    result = C.favourite_add_c(request, id)
    return result

#Cart page function
@login_required
def cart_page(request):
    result = C.cart_page_c(request)
    return result

#Update Cart with items added only (what addtocart button does)
#Update Cart with items added only (what addtocart button does)
#Update Cart with items added only (what addtocart button does)
@login_required
def update_cart(request, id):
    result = C.update_cart_c(request, id)
    return result


@login_required
def update_cart2(request, id):
    result = C.update_cart2_c(request, id)
    return result

#Update Cart with items removed only (what remove button does)
@login_required
def remove_from_cart(request, id):
    result = C.remove_from_cart_c(request, id)
    return result


#Checkout view
@login_required
def checkout(request):
    result = C.checkout_c(request)
    return result

#Confirm payment view
@login_required
def confirm(request, points):
    result = C.confirm_c(request, points)
    return result

def contact_us(request):
    return render(request, 'App1/contact.html')

@login_required
def product_status(request):
    result = C.product_status_c(request)
    return result

@login_required
def edit_product(request,id):
    result = C.edit_product_c(request, id)
    return result


@login_required
def update_product(request,id):
    result = C.update_product_c(request, id)
    return result

@login_required
def remove_product(request, id):
    result = C.remove_product_c(request, id)
    return result

@login_required
def history(request):
    result = C.history_c(request)
    return result

def recommendation_logic(request):
    result = C.recommendation_logic_c(request)
    return result
