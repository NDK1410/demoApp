from django.conf.urls import include, url
from users.views import welcome, register

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^welcome/", welcome, name="welcome"),
    url(r"^register/", register, name="register"),
]