from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from App1 import views

app_name = 'App1'
urlpatterns = [url(r'^register/$', views.register, name = 'register'),
               url(r'^login/$', views.user_login, name = 'user_login'),
               url(r'^logout/$', views.user_logout, name = 'user_logout'),
               url(r'^fill_product/$', views.fill_product_form, name = 'fill_product_form'),
               url(r'^product_details/(?P<id>\w+)/$', views.product_details, name='product_details'),]
