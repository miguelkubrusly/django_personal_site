from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .data import posts

# Create your views here.

def index(request):
  