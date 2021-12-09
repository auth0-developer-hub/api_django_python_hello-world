from django.test import SimpleTestCase
from rest_framework.reverse import reverse

from messages_api.views import (
    PublicMessageApiView, ProtectedMessageApiView, AdminMessageApiView
)


class PublicMessageApiViewTest(SimpleTestCase):

    def test_public_api_view_returns_ok(self):
        response = self.client.get(reverse('public-message'))

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {'text': PublicMessageApiView.text})


class AuthMessageApiViewTest(SimpleTestCase):

    def test_protected_api_view_returns_ok(self):
        response = self.client.get(reverse('protected-message'))

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {'text': ProtectedMessageApiView.text})


class AdminMessageApiViewTest(SimpleTestCase):

    def test_admin_api_view_returns_ok(self):
        response = self.client.get(reverse('admin-message'))

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {'text': AdminMessageApiView.text})
