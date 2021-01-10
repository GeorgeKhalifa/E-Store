from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from App1 import views

app_name = 'App1'
urlpatterns = [url(r'^register/$', views.register, name = 'register'),
               url(r'^login/$', views.user_login, name = 'user_login'),
               url(r'^logout/$', views.user_logout, name = 'user_logout'),
               url(r'^add_product/$', views.add_product, name = 'add_product'),
               url(r'^product_details/(?P<id>\w+)/$', views.product_details, name='product_details'),
               url(r'^fav/(?P<id>\w+)/$', views.favourite_add,name='favourite_add'),
               url(r'^favourites/$', views.favourite_list, name='favourite_list'),
               url(r'^product_status/',views.product_status,name='product_status'),
               url(r'^edit_product/(?P<id>\d+)/$',views.edit_product,name='edit_product'),
               url(r'^update_product/(?P<id>\d+)/$',views.update_product,name='update_product'),
               url(r'^remove_product/(?P<id>\d+)/$',views.remove_product,name='remove_product'),
               ]

