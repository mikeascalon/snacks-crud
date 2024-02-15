from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title="Pickle",
            description="Crunchy, vinegary, and delicious.",  # Assuming description is a string
            purchaser=self.user
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Pickle")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "Pickle")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(f"{self.snack.description}", "Crunchy, vinegary, and delicious.")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pickle")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args=[self.snack.id]))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Pickle")  # Adjust based on your detail view content
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "Rake",
                "description": "A tool",
                "purchaser": self.user.id,
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rake")

    def test_snack_update_view(self):
        response = self.client.post(
            reverse("snack_update", args=[self.snack.id]),
            {"title": "Updated Pickle", "description": "Still crunchy, more vinegary.", "purchaser": self.user.id},
            follow=True,
        )
        self.assertContains(response, "Updated Pickle")

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args=[self.snack.id]))
        self.assertEqual(response.status_code, 200)

    def test_model_str_representation(self):
        self.assertEqual(str(self.snack), "Pickle")