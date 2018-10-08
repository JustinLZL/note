from django.conf.urls import url
from .views import *
urlpatterns = [
    #访问路径是 /
    url(r'^$',index_views),
    #访问路径是 /login
    url(r'^login/$',login_views),
    #访问路径是 /register
    url(r'^register/$',register_views),
]







