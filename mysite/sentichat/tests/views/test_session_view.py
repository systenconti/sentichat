from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AuthViewsTest(TestCase):

    # Create a test user
    def setUp(self):
        self.credentials = {"username": "testuser", "password": "secret"}
        User.objects.create_user(**self.credentials)

    # Test that the login page loads correctly
    def test_login_view_get(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    # Test successful login redirects to main page
    def test_login_view_post_success(self):
        response = self.client.post(reverse("login"), self.credentials, follow=True)
        self.assertTrue(response.context["user"].is_authenticated)
        self.assertRedirects(response, reverse("main"))

    # Test login with incorrect credentials
    def test_login_view_post_failure(self):
        wrong_credentials = {"username": "testuser", "password": "wrong"}
        response = self.client.post(reverse("login"), wrong_credentials)
        self.assertFalse(response.context["user"].is_authenticated)
        self.assertTemplateUsed(response, "login.html")
        self.assertContains(response, "Invalid login credentials")

    # Test logout
    def test_logout_view(self):
        self.client.post(reverse("login"), self.credentials, follow=True)
        response = self.client.get(reverse("logout"), follow=True)
        self.assertFalse(response.context["user"].is_authenticated)
        self.assertRedirects(response, reverse("login"))
