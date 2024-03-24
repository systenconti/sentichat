from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.main_view, name="main"),
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
