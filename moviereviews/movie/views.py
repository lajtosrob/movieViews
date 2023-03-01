from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from movie.models import Item


def about(request):
    return HttpResponse('<h1>Welcome to About page</h1>')

def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', 
                  {'searchTerm': searchTerm})

def todos(request):
    #items= Items.objects all()
    return JsonResponse({"message": "Hello!"})
