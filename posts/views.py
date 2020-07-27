from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the posts index.")

def show(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)