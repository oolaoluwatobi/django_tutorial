from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
  path('register/', views.register_view, name='register'),
  # path('<slug:slug>', views.post_page, name='page'),
]