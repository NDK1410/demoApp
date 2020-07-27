from django.conf.urls import url
 
from . import views

app_name = "user_login"
urlpatterns = [
    url(r'^register$', views.register),
]