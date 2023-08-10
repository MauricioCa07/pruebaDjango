from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Movie

def home (request):
    #return HttpResponse(request,'home.html',{'name':'Greg Lim'})
    #return HttpResponse('<h1>Hola</h1>')
    searchTerm = request.GET.get('searchMovie')
    return render(request,'home.html',{'searchTerm':searchTerm,'movies':searchTerm})

def about(request):
    return render(request,'about.html')
    
