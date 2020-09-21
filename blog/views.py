from django.shortcuts import render
from .models import post

# Create your views here.


def all_posts(request):
    all_posts = post.objects.all()
    return render(request,'post/all_posts.html',{'posts':all_posts})

def single_post(request,id):
    single_post = post.objects.get(id=id)
    return render(request,'post/single_posts.html',{'post':single_post})    