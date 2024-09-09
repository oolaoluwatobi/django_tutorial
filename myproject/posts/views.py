from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts
    }

    return render(request, 'posts/posts_list.html', context)

def post_page(request, slug):

    post = Post.objects.get(slug=slug)
    context = {
        'post': post
    }

    return render(request, 'posts/post_page.html', context)