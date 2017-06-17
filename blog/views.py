from django.shortcuts import render

# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost
from django.utils import timezone

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    return HttpResponse(t.render({'posts': posts}))


def hello(request, article_id):
    text = "<h1>welcome to my app %s!</h1>" % article_id
    return HttpResponse(text)


def new_hello(request):
    today = timezone.datetime.now().date()

    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    return render(request, "hello.html", {"today": today, "days_of_week": daysOfWeek})