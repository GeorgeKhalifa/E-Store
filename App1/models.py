from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)         # Means if the user is deleted, the corresponding user info is also deleted

    BuyerOrSeller = models.CharField(max_length = 30)




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
    details=models.CharField(default='',max_length=2000)
    def get_average_rating(self):
        average = sum(int(review['rating']) for review in self.reviews.values())
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
