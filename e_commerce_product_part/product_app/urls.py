from django.conf.urls import url,include
from product_app import views
from django.urls import path
#template tagging
app_name='product_app'

urlpatterns = [
    url('fillform/',views.fill_product_form,name='form'),
    path('details/<id>',views.details_product,name='details'),
    url('product_list/',views.printproducts,name='product_list'),

]