from django.urls import path
from posts.views import homepage
from django.conf.urls import url

from . import views

app_name = 'posts'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:post_id>/', views.show, name='show'),
    # path('<int:post_id>/', views.show, name='show'),
    path('', views.Index.as_view(), name=''),
    path('<int:pk>/', views.Show.as_view(), name='show'),
]