from django.shortcuts import render
from sentichat.models import ChatRoom
from django.contrib.auth.models import User


def main_view(request):
    user = User.objects.get(username='marektotoszko')
    chatrooms = ChatRoom.objects.filter(participants=user)
    context = {"user": user,
               "chatrooms": chatrooms}
    return render(request, "main.html", context=context)
