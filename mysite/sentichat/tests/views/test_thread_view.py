from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from sentichat.models import ChatRoom, Message


class ChatRoomTestCase(TestCase):
    # Setup test objects
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password123")
        self.user2 = User.objects.create_user(username="user2", password="password123")

        self.chatroom1 = ChatRoom.objects.create(name="Room 1")
        self.chatroom1.participants.add(self.user1)

        self.chatroom2 = ChatRoom.objects.create(name="Room 2")
        self.chatroom2.participants.add(self.user2)

        message1 = Message.objects.create(sender=self.user1, content="Hello Room 1")
        self.chatroom1.messages.add(message1)

        self.client = Client()

    # Test if user gets redirected correctly when not logged in
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse("thread", args=[self.chatroom1.id]))
        self.assertRedirects(response, f"/login/?next=/chatrooms/{self.chatroom1.id}/")

    # Test if user can access his chatroom
    def test_user_can_access_chatroom(self):
        self.client.login(username="user1", password="password123")
        response = self.client.get(reverse("thread", args=[self.chatroom1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "thread.html")
        self.assertIn("messages", response.context)

    # Test if user cannot access someone's chatroom
    def test_user_cannot_access_non_participating_chatroom(self):
        self.client.login(username="user1", password="password123")
        response = self.client.get(reverse("thread", args=[self.chatroom2.id]))
        self.assertEqual(response.status_code, 404)

    # Test for non existent chatroom access
    def test_nonexistent_chatroom_access(self):
        self.client.login(username="user1", password="password123")
        response = self.client.get(reverse("thread", args=[999]))
        self.assertEqual(response.status_code, 404)
