from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Movie

def home (request):
    #return HttpResponse(request,'home.html',{'name':'Greg Lim'})
    #return HttpResponse('<h1>Hola</h1>')
    searchTerm = request.GET.get('searchMovie')

    if searchTerm:
        movies = Movie.objects.filter(tittle__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    return render(request,'home.html',{'searchTerm':searchTerm,'movies':movies})

def about(request):
    return render(request,'about.html')
    
