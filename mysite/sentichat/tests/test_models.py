from django.test import TestCase
from sentichat.models import Message, ChatRoom
from django.contrib.auth.models import User


# Test case for Message model
class MessageModelTest(TestCase):
    # Create user and test message
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.message = Message.objects.create(sender=self.user, content="Hello, World!")

    # Test creation of the Message record
    def test_message_creation(self):
        self.assertEqual(self.message.sender, self.user)
        self.assertEqual(self.message.content, "Hello, World!")

    # Test __str__ method
    def test_message_str(self):
        message_str = f"Message from {self.message.sender.username} sent at {self.message.timestamp}"
        self.assertEqual(str(self.message), message_str)


# Test case for ChatRoomM model
class ChatRoomModelTest(TestCase):
    # Create users, chat_room and messages
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="12345")
        self.user2 = User.objects.create_user(username="user2", password="12345")

        self.chat_room = ChatRoom.objects.create(name="Test Room")

        self.message1 = Message.objects.create(
            sender=self.user1, content="Hello, Room!"
        )
        self.message2 = Message.objects.create(sender=self.user2, content="You too!")

        self.chat_room.participants.add(self.user1, self.user2)

        self.chat_room.messages.add(self.message1, self.message2)

    # Test if the chat_room creation
    def test_chat_room_creation(self):
        self.assertEqual(self.chat_room.name, "Test Room")
        self.assertIn(self.user1, self.chat_room.participants.all())
        self.assertIn(self.user2, self.chat_room.participants.all())
        self.assertIn(self.message1, self.chat_room.messages.all())
        self.assertIn(self.message2, self.chat_room.messages.all())

    # Test chat_room __str__ method
    def test_chat_room_str(self):
        self.assertEqual(str(self.chat_room), "Test Room")
