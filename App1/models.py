from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)         # Means if the user is deleted, the corresponding user info is also deleted

    BuyerOrSeller = models.CharField(max_length = 30)
    offer_points = models.PositiveIntegerField(default=10, blank=True)
    def set_offer_points(self, new_points):
        self.offer_points = new_points
    def get_offer_points(self):
        return self.offer_points

size_choices = (('S','S'),('M','M'),('L','L'),('XL','XL'))
currency_choices = (('$','$'),('€','€'),('L.E','L.E'))
main_category_choices = (('men','Men'),('women','Women'),('kids','Kids'))
secondary_choices = (('top','Top'),('bottom','Bottom'),('coats_jackets','Coats/Jackets'))

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(to = User,on_delete = models.CASCADE)
    name=models.CharField(max_length=20,default='')
    # product_type = models.CharField(max_length = 20, default = "shirt") #product_second_category
    in_stock = models.PositiveIntegerField()
    currency =  models.CharField(default='$',choices=currency_choices,max_length=20)
    size = models.CharField(default='S',choices=size_choices,max_length=20)
    price = models.DecimalField(max_length = 13, decimal_places = 2, max_digits = 10) #product_price
    picture = models.ImageField(upload_to = 'product_picture/', default = 'null.png')
    main_category= models.CharField(default='Men',choices=main_category_choices,max_length=20)
    secondary_category=  models.CharField(default='Top',choices=secondary_choices,max_length=20)
    details=models.CharField(default='',max_length=1999)
#    discount = models.DecimalField(max_length = 13, decimal_places = 2, max_digits = 10) #product_price
    views = models.ManyToManyField(User,related_name='view',default=None,blank=True)

    favourites =models.ManyToManyField(User,related_name='favourite',default=None,blank=True)
    def get_average_rating(self):
        review = ProductReview.objects.filter(product = self)
        average = sum(int(rev.get_rating()) for rev in review)
        #average = sum(int(review['rating']) for review in self.reviews.values())
        count = self.reviews.count()
        if count > 0:
            return round(average/count, 1)
        else:
            return 0



class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete = models.CASCADE)
    review_content = models.TextField(blank = True, null = True)
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def get_rating (self):
        return self.rating

payment_choices = (('cod','COD(Cash on delivery)'),('credit','Credit Card'))
class Order (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default=None, null=True)
    address = models.CharField(max_length=99)
    phone_number = models.CharField(max_length=11)
    zip_code = models.CharField(max_length=4)
    currency =  models.CharField(default='$', choices=currency_choices, max_length=20)
    payment_method = models.CharField(default='cod', choices=payment_choices, max_length=20)
    total_cost = models.FloatField(default=0.00, max_length=6)
    new_total_cost = models.FloatField(max_length=10, default=0.00)
    discount_points = models.CharField(max_length=4)
    purchase_date = models.DateTimeField(default = None, null = True, blank = True)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    item = models.ForeignKey(Product, on_delete = models.CASCADE) 
    quantity = models.PositiveIntegerField(default = 1) #still needed to be less than item.in_stock
    total_item_price = models.FloatField(max_length=6, default = 100.00) #still needed to be default the item price & quantity*item.price
    purchased = models.BooleanField(default = False)
    in_order = models.ForeignKey(Order, on_delete = models.SET_NULL, null=True)
    #we need to implement a view to add a cartitem and/or increase its quantity
    #we need to implement a view to remove a cartitem to be accessed from cart_page.html
    #we need to implement a view to calculate the total_item_price 

