from django import forms

# from .models import Post
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'banner']

    # def __init__(self, *args, **kwargs):
    #     super(CreatePost, self).__init__(*args, **kwargs)