from django.shortcuts import render, get_object_or_404
from .models import Post, Group

COUNT_POSTS = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.select_related('group', 'author').all()[:COUNT_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.select_related('group', 'author').all()[:COUNT_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
