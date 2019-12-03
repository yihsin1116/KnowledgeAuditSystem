from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'homepage.html')

def links(request):
  return render(request, 'link.html')