from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=75)
    age = models.TextField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self):
        return self.title