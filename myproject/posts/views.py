from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms



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

@login_required(login_url='/users/login/')
def post_new(request):
    if request.method == 'POST':
        form = form.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save with user
            return redirect('posts:list')
    else:
        form = forms.CreatePost()

    return render(request, 'posts/post_new.html', { 'form': form })