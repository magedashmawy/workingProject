from django.conf.urls import url

from products.views import product_LView
from . import views



app_name = 'products'
urlpatterns = [
    # /products/
   # url(r'^products-fbv/$', product_LView),


    # /products/<album_id>/"""
   # url(r'^(?P<album_id>[0-9]+)/$' , views.details, name="detail"),


]
