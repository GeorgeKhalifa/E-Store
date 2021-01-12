from django.test import TestCase,RequestFactory
#from django.test import TestCase
from App1.models import Product,UserInfo,ProductReview,CartItem,Order
# from django.contrib.auth.models import User
from django.contrib.auth.models import User,AnonymousUser
from datetime import date,datetime
from App1.views import index,index_sort_price,index_sort_newest,index_sort_rating,index_category,index_category1,index_category2,index_category3,index_category4,index_category5,register,user_login,user_logout,add_product,product_details,favourite_list,favourite_add,cart_page,update_cart,update_cart2,remove_from_cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.test.client import Client
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponseRedirect
# import unittest


# Create your tests here.
#User=get_user_model()
#user_a.save()
#user_a_info=UserInfo.objects.create(BuyerOrSeller='seller')
#user_a_info.save(commit = false)
#user_a_info.user = user_a
#user_a_info.save()
class ProductTestCase(TestCase):
    def setUp(self):
        user_a=User.objects.create_user(first_name='johnn',last_name='emad',email='j@test.com',username='john',password='1234')
        user_a_info=UserInfo.objects.create(user = user_a, BuyerOrSeller='seller')

        obj1=Product.objects.create(seller = user_a,name='t-shirt',price=200,size='s',currency='$',main_category='men',secondary_category='top',in_stock=12)
        obj2=Product.objects.create(seller = user_a,name='coat',price=500,size='l',currency='$',main_category='women',secondary_category='coats_jackets',in_stock=2)
        ProductReview.objects.create(product=obj1, user=user_a, review_content="any text", rating=3)
        ProductReview.objects.create(product=obj1, user=user_a, review_content="any text", rating=4)

    def test_Product_test(self):
          obj1=Product.objects.get(name='t-shirt')
          obj2=Product.objects.get(name='coat')
        #   ProductReview.objects.create(product=obj1, user=user_a, review_content="any text", rating=3)
        #   ProductReview.objects.create(product=obj1, user=user_a, review_content="any text", rating=4)
          self.assertEqual(obj1.name,'t-shirt')
          self.assertEqual(obj2.name,'coat')
          self.assertEqual(obj1.price,200)
          self.assertEqual(obj2.price,500)
          self.assertEqual(obj1.currency,'$')
          self.assertEqual(obj2.currency,'$')
          self.assertEqual(obj1.size,'s')
          self.assertEqual(obj2.size,'l')
          self.assertEqual(obj1.main_category,'men')
          self.assertEqual(obj2.main_category,'women')
          self.assertEqual(obj1.secondary_category,'top')
          self.assertEqual(obj2.secondary_category,'coats_jackets')
          self.assertEqual(obj1.in_stock,12)
          self.assertEqual(obj2.in_stock,2)
          self.assertEqual(obj1.get_average_rating(),3.5)

class ProductReviewTestCase(TestCase):
    def setUp(self):
         user_a=User.objects.create_user(first_name='johnn',last_name='emad',email='j@test.com',username='john',password='1234')
         user_a_info=UserInfo.objects.create(user = user_a, BuyerOrSeller='seller')

         product1=Product.objects.create(seller = user_a,name='t-shirt',price=200,size='s',currency='$',main_category='men',secondary_category='top',in_stock=12)
         product2=Product.objects.create(seller = user_a,name='coat',price=500,size='l',currency='$',main_category='women',secondary_category='coats_jackets',in_stock=2)

         ProductReview.objects.create(product=product1, user=user_a, review_content="any text", rating=3)
         ProductReview.objects.create(product=product1, user=user_a, review_content="any text", rating=4)

    def test_ProductReview_test(self):
          product_review1=ProductReview.objects.get(rating=4)
          self.assertEqual(product_review1.review_content,"any text")
          self.assertEqual(product_review1.rating,4)
          self.assertEqual(product_review1.get_rating(),4)
          #   self.assertEqual(product_review1.date,datetime.now())
          product_review2=ProductReview.objects.get(rating=3)
          self.assertEqual(product_review2.review_content,"any text")
          self.assertEqual(product_review2.rating,3)
          self.assertEqual(product_review2.get_rating(),3)
         #   self.assertEqual(product_review2.date,datetime.now())

class CartItemTestCase(TestCase):
    def setUp(self):
         user_b=User.objects.create_user(first_name='johnnn',last_name='emadd',email='jj@test.com',username='jo',password='1234')
         user_b_info=UserInfo.objects.create(user = user_b, BuyerOrSeller='buyer')
         user_a=User.objects.create_user(first_name='johnn',last_name='emad',email='j@test.com',username='john',password='1234')
         user_a_info=UserInfo.objects.create(user = user_a, BuyerOrSeller='seller')

         product1=Product.objects.create(seller = user_a,name='t-shirt',price=200,size='s',currency='$',main_category='men',secondary_category='top',in_stock=12)
         product2=Product.objects.create(seller = user_a,name='coat',price=500,size='l',currency='$',main_category='women',secondary_category='coats_jackets',in_stock=2)
         product3=Product.objects.create(seller = user_a,name='shirt',price=50,size='m',currency='$',main_category='kids',secondary_category='top',in_stock=1)

         cart_item1=CartItem.objects.create(item=product1,user=user_b,quantity=10,total_item_price=10*product1.price)
         cart_item2=CartItem.objects.create(item=product2,user=user_b,quantity=2,total_item_price=2*product2.price)
         cart_item3=CartItem.objects.create(item=product3,user=user_b)

    def test_CartItem_test(self):
        product1=Product.objects.get(name='t-shirt')
        cart_item1=CartItem.objects.get(item=product1)
        self.assertEqual(cart_item1.quantity,10) 
        self.assertEqual(cart_item1.total_item_price,2000)
        self.assertEqual(cart_item1.purchased,False)
        product2=Product.objects.get(name='coat')
        cart_item2=CartItem.objects.get(item=product2)
        self.assertEqual(cart_item2.quantity,2) 
        self.assertEqual(cart_item2.total_item_price,1000)
        self.assertEqual(cart_item2.purchased,False)
        product3=Product.objects.get(name='shirt')
        cart_item3=CartItem.objects.get(item=product3) 
        self.assertEqual(cart_item3.quantity,1) #the default value of the quantity=1#
        self.assertEqual(cart_item3.total_item_price,100) #the default value of the total_item_price=100#
        self.assertEqual(cart_item3.purchased,False)
        
class OrderTestCase(TestCase):
    def setUp(self):
        user_a=User.objects.create_user(first_name='johnn',last_name='emad',email='j@test.com',username='john',password='1234')
        user_a_info=UserInfo.objects.create(user = user_a, BuyerOrSeller='buyer')

        Order.objects.create(user=user_a,address="abdu-basha",phone_number="01234567890",zip_code="1234",currency="$",payment_method="cod",total_cost=1000,discount_points="10")
    
    def test_Order_test(self):
        order1=Order.objects.get(address="abdu-basha")
        user_a=User.objects.get(first_name='johnn')
        self.assertEqual(order1.user,user_a)
        self.assertEqual(order1.phone_number,'01234567890')
        self.assertEqual(order1.zip_code,'1234')
        self.assertEqual(order1.currency,'$')
        self.assertEqual(order1.payment_method,'cod')
        self.assertEqual(order1.total_cost,1000)
        self.assertEqual(order1.discount_points,"10")





        












class SimpleTest(TestCase):
    def setUp(self):
        self.client=Client()
        self.factory=RequestFactory()
        self.user=User.objects.create_user(first_name='jacob',last_name='messi',email='jacob@test.com',username='leo',password='1234')
        self.user_info= UserInfo.objects.create(user = self.user, BuyerOrSeller='buyer')


    def test_index(self):
        request=self.factory.get('App1/index')
        request.user=AnonymousUser()
        request.user=self.user
        response=index(request)

    def test_index_sort_price(self):
        request=self.factory.get('App1/index_sort_price')
        request.user=AnonymousUser()
        request.user=self.user
        response=index_sort_price(request)

    def test_index_sort_newest(self):
        request=self.factory.get('App1/index_sort_newest')
        request.user=AnonymousUser()
        request.user=self.user
        response=index_sort_newest(request)

    def test_index_sort_rating(self):
        request=self.factory.get('App1/index_sort_rating')
        request.user=AnonymousUser()
        request.user=self.user
        response=index_sort_rating(request)

    def test_index_category(self):
        request=self.factory.get('App1/index_category')
        request.user=AnonymousUser()
        request.user=self.user
        response=index_category(request)

    def test_index_category1(self):
        request=self.factory.get('App1/index_category1')
        request.user=AnonymousUser()
        request.user=self.user
        response=index_category1(request)

    def test_index_category2(self):
        request=self.factory.get('App1/index_category2')
        request.user=AnonymousUser()
        request.user=self.user
        response=index_category2(request)

    def test_index_category3(self):
        request=self.factory.get('App1/index_category3')
        request.user=AnonymousUser()
        request.user=self.user
        response=index_category3(request)

    def test_index_category4(self):
        request=self.factory.get('App1/index_category4')
        request.user=AnonymousUser()
        request.user=self.user
        response=index_category4(request)

    def test_index_category5(self):
        request=self.factory.get('App1/index_category5')
        request.user=AnonymousUser()
        request.user=self.user
        response=index_category5(request)

    def test_register(self):
        request=self.factory.get('App1/register')
        request.user=self.user
        response=register(request)

    def test_user_login(self):
        request=self.factory.get('App1/user_login')
        request.user=self.user
        response=user_login(request)

    def test_user_logout(self):
       self.client.login(username='leo',password='1234')
       response=self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200)
    



    
    def test_add_product(self):
        request=self.factory.get('App1/add_product')
        request.user=self.user
        response=add_product(request)

    def test_product_details(self):
        request=self.factory.get('App1/product_details')
        request.user=self.user
        user_a=User.objects.create_user(first_name='johnn',last_name='emad',email='j@test.com',username='john',password='1234')
        user_a_info=UserInfo.objects.create(user = user_a, BuyerOrSeller='seller')
        product=Product.objects.create(seller = user_a,name='t-shirt',price=200,size='s',currency='$',main_category='men',secondary_category='top',in_stock=12)
        x=id(product)
        response=product_details(request,1)
    
    def test_favourite_list(self):
        request=self.factory.get('App1/favourites')
        request.user=self.user
        response=favourite_list(request)
    
    # def test_favourite_add1(self):
    #     HttpResponseRedirect=self.factory.get('App1/favourites')
    #     HttpResponseRedirect.user=self.user
    #     user_a=User.objects.create_user(first_name='johnn',last_name='emad',email='j@test.com',username='john',password='1234')
    #     user_a_info=UserInfo.objects.create(user = user_a, BuyerOrSeller='seller')
    #     product=Product.objects.create(seller = user_a,name='t-shirt',price=200,size='s',currency='$',main_category='men',secondary_category='top',in_stock=12)
    #     x=id(product)
    #     HttpResponseRedirect=favourite_add(HttpResponseRedirect.META['HTTP_REFERER'],1)

    def test_favourite_add(self):
        self.client.login(username='leo',password='1234')
        user_a=User.objects.create_user(first_name='johnn',last_name='emad',email='j@test.com',username='john',password='1234')
        user_a_info=UserInfo.objects.create(user = user_a, BuyerOrSeller='seller')
        product=Product.objects.create(seller = user_a,name='t-shirt',price=200,size='s',currency='$',main_category='men',secondary_category='top',in_stock=12)
        url='App1/fav/(?P<id>\w+)/'
        response=self.client.get(url,id=1)
        self.assertEqual(response.status_code, 404)
    
    def test_cart_page(self):
         request=self.factory.get('App1/cart_page')
         request.user=self.user
         response=cart_page(request)

    def test_update_cart(self):
        self.client.login(username='leo',password='1234')
        user_a=User.objects.create_user(first_name='johnn',last_name='emad',email='j@test.com',username='john',password='1234')
        user_a_info=UserInfo.objects.create(user = user_a, BuyerOrSeller='seller')
        product=Product.objects.create(seller = user_a,name='t-shirt',price=200,size='s',currency='$',main_category='men',secondary_category='top',in_stock=12)
        url='App1/update_cart/(?P<id>\w+)/'
        response=self.client.get(url,id=1)
        self.assertEqual(response.status_code, 404)
    
    def test_update_cart2(self):
        self.client.login(username='leo',password='1234')
        user_a=User.objects.create_user(first_name='johnn',last_name='emad',email='j@test.com',username='john',password='1234')
        user_a_info=UserInfo.objects.create(user = user_a, BuyerOrSeller='seller')
        product=Product.objects.create(seller = user_a,name='t-shirt',price=200,size='s',currency='$',main_category='men',secondary_category='top',in_stock=12)
        url='App1/update_cart2/(?P<id>\w+)/'
        response=self.client.get(url,id=1)
        self.assertEqual(response.status_code, 404)

    def test_remove_from_cart(self):
        self.client.login(username='leo',password='1234')
        user_a=User.objects.create_user(first_name='johnn',last_name='emad',email='j@test.com',username='john',password='1234')
        user_a_info=UserInfo.objects.create(user = user_a, BuyerOrSeller='seller')
        product=Product.objects.create(seller = user_a,name='t-shirt',price=200,size='s',currency='$',main_category='men',secondary_category='top',in_stock=12)
        url='App1/remove_from_cart/(?P<id>\w+)/'
        response=self.client.get(url,id=1)
        self.assertEqual(response.status_code, 404)
        





       

    


    
    
       
    
         
                




        





