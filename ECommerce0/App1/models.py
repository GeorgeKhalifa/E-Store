from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
# Create your models here.
#Habiba
class UserInfo (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)         # Means if the user is deleted, the corresponding user info is also deleted

    BuyerOrSeller = models.CharField(max_length = 30)

#George
class Product(models.Model):
    size_choices = (('small','S'),('medium','M'),('large','L'))
    currency_choices = (('dollar','$'),('euro','€'),('egyption_pound','L.E'))
    main_category_choices = (('men','Men'),('women','Women'),('kids','Kids'))
    secondary_choices = (('top','Top'),('bottom','Bottom'),('coats_jackets','Coats/Jackets'))

    product_seller = models.ForeignKey(to = User, on_delete = models.CASCADE) #updated by Habiba
    product_name=models.CharField(max_length=20)
    product_price=models.IntegerField(default=0)
    product_size = models.CharField(default='S',choices=size_choices,max_length=20)
    product_amount = models.IntegerField(default=0)
    product_currency =  models.CharField(default='$',choices=currency_choices,max_length=20)
    product_main_category= models.CharField(default='Men',choices=main_category_choices,max_length=20)
    product_secondary_category=  models.CharField(default='Top',choices=secondary_choices,max_length=20)
    product_picture = models.ImageField(upload_to='product_pictures',blank=True)
    product_details=models.CharField(default='',max_length=2000)
    #product_reviews = models.CharField(default='',max_length=2000)#Removed by Habiba
    # product_color = ColorField(default='')
    def __str__(self):
        return self.product_name
    def get_average_rating(self):#Habiba
        average = sum(int(review['rating']) for review in self.reviews.values())
        count = self.reviews.count()
        if count > 0:
            return round(average/count, 1)
        else:
            return 0

#Habiba
class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete = models.CASCADE)
    review_content = models.TextField(blank = True, null = True)
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
