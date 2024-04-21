from django.shortcuts import render, get_object_or_404
from sentichat.models import ChatRoom
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def thread_view(request, chatroom_id):
    chatroom = get_object_or_404(ChatRoom, id=chatroom_id)
    if request.user not in chatroom.participants.all():
        raise Http404("You do not have permission to view this chatroom.")
    
    messages = chatroom.messages.all().order_by('timestamp')
    context = {'chatroom': chatroom, 'messages': messages}
    return render(request, "thread.html", context=context)
