from django.conf.urls import *
from blog.views import archive, hello

urlpatterns = [url(r'^start', archive),
               url(r'^hello/', hello), ]