from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    return HttpResponse('<h1>good morning Tabby</h1>')

def login(request):
    return HttpResponse("<h1>welcome to your login page</h1>")



# Create your views here.
