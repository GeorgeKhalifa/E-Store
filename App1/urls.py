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
               url(r'^cart/$', views.cart_page, name = 'cart'),
               url(r'^update_cart/(?P<id>\w+)/$', views.update_cart, name='update_cart'),
               url(r'^cart/remove_from_cart/(?P<id>\w+)/$', views.remove_from_cart, name='remove_from_cart'),
               url(r'^cart/update_cart2/(?P<id>\w+)/$', views.update_cart2, name='update_cart2'),
               url(r'^checkout/$', views.checkout, name = 'checkout'),
               url(r'^checkout2/$', views.checkout2, name = 'checkout2'),
               url(r'^checkout3/$', views.checkout3, name = 'checkout3'),
               url(r'^confirm/$', views.confirm, name = 'confirm'),
               url(r'^contact/$',views.contact_us, name='contact'),
               url(r'^product_status/',views.product_status,name='product_status'),
               url(r'^edit_product/(?P<id>\d+)/$',views.edit_product,name='edit_product'),
               url(r'^update_product/(?P<id>\d+)/$',views.update_product,name='update_product'),
               url(r'^remove_product/(?P<id>\d+)/$',views.remove_product,name='remove_product'),
               url(r'^history/$', views.history, name = 'history'),
               url(r'^views/$', views.view_list, name='view_list'),
               url(r'^filtered_views/$', views.recommendation_logic, name='recommendation_logic'),
]
#
