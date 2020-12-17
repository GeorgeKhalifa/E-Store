from django.db import models
from colorfield.fields import ColorField
# Create your models here.
class Product(models.Model):
    size_choices = (('small','S'),('medium','M'),('large','L'))
    currency_choices = (('dollar','$'),('euro','€'),('egyption_pound','L.E'))
    main_category_choices = (('men','Men'),('women','Women'),('kids','Kids'))
    secondary_choices = (('top','Top'),('bottom','Bottom'),('coats_jackets','Coats/Jackets'))

    #product_seller = models.ForeignKey(User/Seller)
    product_name=models.CharField(max_length=20)
    product_price=models.IntegerField(default=0)
    product_size = models.CharField(default='S',choices=size_choices,max_length=20)
    product_amount = models.IntegerField(default=0)
    product_currency =  models.CharField(default='$',choices=currency_choices,max_length=20)
    product_main_category= models.CharField(default='Men',choices=main_category_choices,max_length=20)
    product_secondary_category=  models.CharField(default='Top',choices=secondary_choices,max_length=20)
    product_picture = models.ImageField(upload_to='product_pictures',blank=True)
    product_details=models.CharField(default='',max_length=2000)
    product_reviews = models.CharField(default='',max_length=2000)
    # product_color = ColorField(default='')


    def __str__(self):
        return self.product_name
    
