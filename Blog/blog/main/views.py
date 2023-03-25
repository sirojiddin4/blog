from django.shortcuts import render
from django.http import Http404
# Create your views here.

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request, 'templates/blog/post/list.html', {'posts': posts})

def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)

    except Post.DoesNotExist:
        raise Http404(
            'No Post found'
        )
    return render(request, 'templates/blog/post/detail.html', {'post': post})
