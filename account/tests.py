from django.test import TestCase
from .models import User

class UserModelTestCase(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(email='testuser@example.com', password='password123')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.check_password('password123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(email='superuser@example.com', password='password123')
        self.assertEqual(superuser.email, 'superuser@example.com')
        self.assertTrue(superuser.check_password('password123'))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError) as context:
            User.objects.create_user(email='', password='password123')
        self.assertTrue('Please enter a valid email address' in str(context.exception))

    def test_create_superuser_without_email(self):
        with self.assertRaises(ValueError) as context:
            User.objects.create_superuser(email='', password='password123')
        self.assertTrue('Please enter a valid email address' in str(context.exception))
