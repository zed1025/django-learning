from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(ListView):
	model = Post
	template_name = 'home.html'


class BlogDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'
	# the context object returned is named 'post', from the model or 'object'. Can use both in templates or specify something you like using context_object_name
	

class BlogCreateView(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = ['title', 'body', 'author']
	

class BlogUpdateView(UpdateView):
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'body']
	

class BlogDeleteView(DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')