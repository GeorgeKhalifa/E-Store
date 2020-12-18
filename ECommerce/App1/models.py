from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
# Create your models here.

class UserInfo (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)         # Means if the user is deleted, the corresponding user info is also deleted

    BuyerOrSeller = models.CharField(max_length = 30)



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(to = User,on_delete = models.CASCADE)
    product_type = models.CharField(max_length = 20, default = "shirt")
    in_stock = models.PositiveIntegerField()
    Color = ColorField(default = '#FF0000')
    price = models.DecimalField(max_length = 13, decimal_places = 2, max_digits = 10)
    picture = models.ImageField(upload_to = 'product_picture/', default = 'null.png')
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
