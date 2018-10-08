from django.shortcuts import render
from .forms import *

# Create your views here.
def index_views(request):
    return render(request,'index.html')

# /login 对应的视图
def login_views(request):
    form = LoginForm()
    return render(request,'login.html',locals())

# /register 对应的视图
def register_views(request):
    return render(request,'register.html')

