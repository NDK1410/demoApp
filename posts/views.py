from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

class Index(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'
    paginator = Paginator(context_object_name, 4)
    page_obj = paginator.get_page(page_number)

    def get_queryset(self, request):
        page_number = request.GET.get('page')
        return (Post.objects.order_by('-pub_date')[:6], {'page_number':page_number})


class Show(generic.DetailView):
    model = Post
    template_name = 'posts/show.html'
