from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse("Hello World, This is my new HOME !")

def about(request):
    return HttpResponse("This website streams the latest movies")