from django.shortcuts import render
from datetime import datetime, timezone
from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post

    def get_context_data(self, *, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_qty'] = len(Post.objects.all())
        return context

    def get_queryset(self):
        qset = super().get_queryset()
        return qset.order_by('-id', '-date_created')


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

