from django.test import TestCase
from rest_framework.test import APITestCase

from users.models import User


# class UserModelTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             name='Test user',
#             email='test@test.kz',
#             age=12,
#             is_active=True
#         )
#
#     def test_user_creation(self):
#         user = User.objects.get(email='test@test.kz')
#
#         self.assertEqual(self.user, user)
#
#     def test_user_name(self):
#         self.assertEqual(self.user.name, 'Test user')
#         self.assertEqual(self.user.email, 'test@test.kz')



class UserApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Test user',
            email='test@test.kz',
            age=12,
            is_active=True
        )

    def test_get_users(self):
        response = self.client.get('/users_api/v6/users/')

        self.assertEqual(response.status_code, 200)

        self.assertGreater(len(response.data), 0)

    def test_get_len_users(self):
        response = self.client.get('/users_api/v6/users/')

        self.assertGreater(len(response.data), 0)

    def test_post_user(self):
        data = {
            'name': 'Alisher',
            'age': 19,
            'email': 'alisher_test@test.kz',
            'is_active': True
        }

        response = self.client.post('/users_api/v6/users/', data)

        self.assertEqual(response.status_code, 201)



