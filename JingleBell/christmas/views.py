from django.shortcuts import render
from django.http import HttpResponse
from .models import Decoration
from django.template import loader
# Create your views here.

def welcome(request):
    return HttpResponse("Hello, world. Merry Christmas.")
    
def detail(request, location):
    return HttpResponse("You're looking at location %s." % location)
    
def index(request,location):
    return render(request, 'christmas/index.html', {'location': location})
