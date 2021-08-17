from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    response= requests.get('https://codeforces.com/api/user.info?handles=parthivsarkar360').json()
    
    return render(request, "page/home.html", {'response': response})

