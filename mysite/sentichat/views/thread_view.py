from django.shortcuts import render, get_object_or_404
from sentichat.models import ChatRoom
from django.contrib.auth.decorators import login_required
from django.http import Http404
from sentichat.forms import MessageForm
from django.shortcuts import redirect


@login_required
def thread_view(request, chatroom_id):
    chatrooms = ChatRoom.objects.filter(participants=request.user)
    chatroom = get_object_or_404(ChatRoom, id=chatroom_id)
    if request.user not in chatroom.participants.all():
        raise Http404("You do not have permission to view this chatroom.")

    messages = chatroom.messages.all().order_by("timestamp")
    form = MessageForm()
    context = {
        "chatrooms": chatrooms,
        "chatroom": chatroom,
        "messages": messages,
        "form": form,
    }
    return render(request, "thread.html", context=context)


def send_message(request, chatroom_id):
    chatroom = get_object_or_404(ChatRoom, id=chatroom_id)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            chatroom.messages.add(message)
            return redirect("thread", chatroom_id=chatroom_id)
    return redirect("thread", chatroom_id=chatroom_id)
