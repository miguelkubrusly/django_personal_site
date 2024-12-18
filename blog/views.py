from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .data.posts import posts

# Create your views here.

def home(request):
  res = render(request, "blog/home.html",{
    "posts": [posts[0], posts[1], posts[2]]
  })
  return res