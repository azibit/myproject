from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    return HttpResponse(t.render({'posts': posts}))


def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)