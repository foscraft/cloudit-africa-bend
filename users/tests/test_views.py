from typing import Any

from django.contrib.auth import get_user_model
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .mocks import test_user, test_user_2

fake = Faker()
User = get_user_model()


class TestUserList(APITestCase):
    user: Any

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(**test_user)

    @property
    def bearer_token(self) -> str:
        login_url = reverse("login")
        response = self.client.post(
            login_url,
            data={
                "email": test_user["email"],
                "password": test_user["password"],
            },
            format="json",
        )
        return response.data.get("access")  # type: ignore[no-any-return,attr-defined]

    def test_create_user(self) -> None:
        url = reverse("user-list")
        data = {
            "username": fake.user_name(),
            "email": fake.email(),
            "password": fake.password(),
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self) -> None:
        url = reverse("login")
        response = self.client.post(
            url,
            data={
                "email": test_user["email"],
                "password": test_user["password"],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_list(self) -> None:

        url = reverse("user-list")
        self.client.credentials(  # type: ignore[attr-defined]
            HTTP_AUTHORIZATION=f"Bearer {self.bearer_token}"
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user_with_existing_email(self) -> None:
        url = reverse("user-list")
        data = {
            "username": fake.user_name(),
            "email": self.user.email,
            "password": fake.password(),
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestUserDetail(APITestCase):
    user: Any

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(**test_user_2)

    @property
    def bearer_token(self) -> str:
        login_url = reverse("login")
        response = self.client.post(
            login_url,
            data={
                "email": test_user_2["email"],
                "password": test_user_2["password"],
            },
            format="json",
        )
        return response.data.get("access")  # type: ignore[no-any-return,attr-defined]

    def test_get_user_detail(self) -> Any:
        url = reverse("user-detail", kwargs={"lookup_id": self.user.lookup_id})
        self.client.credentials(  # type: ignore[attr-defined]
            HTTP_AUTHORIZATION=f"Bearer {self.bearer_token}"
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail_with_invalid_id(self) -> None:
        self.client.credentials(  # type: ignore[attr-defined]
            HTTP_AUTHORIZATION=f"Bearer {self.bearer_token}"
        )
        url = reverse("user-detail", kwargs={"lookup_id": -1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_user(self) -> None:
        self.client.credentials(  # type: ignore[attr-defined]
            HTTP_AUTHORIZATION=f"Bearer {self.bearer_token}"
        )
        url = reverse("user-detail", kwargs={"lookup_id": self.user.lookup_id})
        username = fake.user_name()
        response = self.client.patch(url, data={"username": username})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("username"), username)  # type: ignore[attr-defined]

    def test_delete_user(self) -> None:
        self.client.credentials(  # type: ignore[attr-defined]
            HTTP_AUTHORIZATION=f"Bearer {self.bearer_token}"
        )
        url = reverse("user-detail", kwargs={"lookup_id": self.user.lookup_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
