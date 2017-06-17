from django.conf.urls import *
from blog.views import archive, hello, new_hello

urlpatterns = [url(r'^start', archive),
               url(r'^hello/(\d+)/', hello, name="hello"),
               url(r'^new_hello', new_hello),
               ]