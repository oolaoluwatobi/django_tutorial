from django.shortcuts import render

# Create your views here.
def user_register(request):
    return render(request, 'users/user_register.html')
    # posts = Post.objects.all().order_by('-created_at')
    # context = {
    #     'posts': posts
    # }

    # return render(request, 'posts/posts_list.html', context)

