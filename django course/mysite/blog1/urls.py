# this url file is created by me
from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path("", views.index, name="BlogHome")
]