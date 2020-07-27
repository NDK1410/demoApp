from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:4]
	context = {'latest_post_list': latest_post_list}
	return render(request, 'posts/index.html', context)

def show(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'posts/show.html', {'post': post})
