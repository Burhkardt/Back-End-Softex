from django.shortcuts import render
from .models import Post
from django.contrib.auth import get_user_model

# Create your views here.
def post_list(request):
    User = get_user_model()
    post = Post.objects.filter(Autor = User.objects.get(username="Juli").id)
    return render(request, 'blog/post_list.html', {'posts':post})