from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/create.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/update.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'



class PostDelete
