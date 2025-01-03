from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .data.posts import posts

# Create your views here.

def home(req):
  first_posts = posts[:3]
  res = render(req, "blog/home.html",{
    "posts": first_posts
  })
  return res

def index(req):
  res = render(req, "blog/index.html", {
    "posts":posts
  })
  return res

def redirect_details(req, num):
  redirected_url = reverse("post-details", args=[posts[num-1]])
  return HttpResponseRedirect(redirected_url)

def details(req, slug):
  post = next((post for post in posts if post.get("slug")==slug), None)
  if post != None:
    post_html = render(req, "blog/details.html", {
      "post": post
    })
    return post_html
  else:
    raise Http404
  