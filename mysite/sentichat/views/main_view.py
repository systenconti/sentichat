from django.shortcuts import render
from sentichat.models import ChatRoom
from django.contrib.auth.decorators import login_required


@login_required
def main_view(request):
    user = request.user
    chatrooms = ChatRoom.objects.filter(participants=user)
    context = {"user": user, "chatrooms": chatrooms}
    return render(request, "main.html", context=context)
