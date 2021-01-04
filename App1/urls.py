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
               url(r'^index_category/$', views.index_category, name = 'index_category'),
               url(r'^index_category1/$', views.index_category1, name = 'index_category1'),
               url(r'^index_category2/$', views.index_category2, name = 'index_category2'),
               url(r'^index_sort_price/$', views.index_sort_price, name = 'index_sort_price'),
               url(r'^index_sort_newest/$', views.index_sort_newest, name = 'index_sort_newest'),
               url(r'^index_sort_rating/$', views.index_sort_rating, name = 'index_sort_rating'),
               url(r'^index_category3/$',views.index_category3, name='index_category3'),
               url(r'^index_category4/$',views.index_category4, name='index_category4'),
               url(r'^index_category5/$',views.index_category5, name='index_category5'),
               ]
#
