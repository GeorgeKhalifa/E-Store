from django.contrib import admin
from App1.models import UserInfo, Product, ProductReview, CartItem

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(CartItem)

