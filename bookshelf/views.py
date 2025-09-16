from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser

def home(request):
    return HttpResponse("Welcome to the Library Project!")

def book_list(request):
    return render(request, "bookshelf/book_list.html", {})
