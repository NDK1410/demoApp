from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.template.response import TemplateResponse

from .models import Post

def homepage(request):
    return redirect('/welcome')

class Index(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:6]

class Show(generic.DetailView):
    model = Post
    template_name = 'posts/show.html'