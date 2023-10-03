from django.urls import path
from .import views


urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name='about'),
    path("contact",views.contact,name="contact"),
    path("tracking",views.tracking,name="tracking"),
    path("search", views.search,name="search"),
    path("productview", views.productview, name="productview"),
    path("checkout",views.checkout,name='checkout')
]