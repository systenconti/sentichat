from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_view, name="main"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("chatrooms/<int:chatroom_id>/", views.thread_view, name="thread"),
]
