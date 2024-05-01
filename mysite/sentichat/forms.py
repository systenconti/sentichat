from django.forms import ModelForm
from sentichat.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            "content",
        ]
