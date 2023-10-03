from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):  
    allProds = []
    #Retrieves unique product categories from the "Product" model
    catProds = Product.objects.values('category')
    # Creates a set of unique product categories from the data collected in the previous step.
    cats = {item['category'] for item in catProds}
    # Iterates through each unique product category.
    for cat in cats:
        # Retrieves all products that belong to the current category and stores them in the "prod" variable.
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        # This line calculates the number of slides needed for your carousel
        no_slides = n//4 + ceil((n/4) - (n//4))
        # Adds a list to "allProds" containing the products in the current category, a range of numbers from 1 to the calculated number of slides, and the total number of slides.
        allProds.append([prod,range(1,no_slides), no_slides])
        
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')
    
def contact(request):
    return HttpResponse("We are at Contact section")

def tracking(request):
    return HttpResponse("We are at Tracking section")

def search(request):
    return HttpResponse("We are at search section")

def productview(request):
    return HttpResponse("We are at productview section")

def checkout(request):
    return HttpResponse("We are at Checkout section")