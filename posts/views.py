from django.shortcuts import render
from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:4]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'posts/index.html', context)

def show(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)