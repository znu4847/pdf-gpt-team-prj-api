from rest_framework.test import APITestCase
from users.models import User

# Create your tests here.

BASE_URL = "/api/v1/users"


# test users
test_users = [
    "test_user1",
    "test_user2",
    "test_user3",
]


# create test users
def create_user(username="test_user", password="test_password"):
    return User.objects.create_user(
        username=username,
        password=password,
    )


class RootTestCase(APITestCase):

    URL = f"{BASE_URL}/"

    def setUp(self):
        for user in test_users:
            create_user(user)

    def test_get(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200, "ROOT get #1")
        self.assertEqual(len(response.data), 3, "ROOT get #2")

    def test_post_success(self):
        response = self.client.get(self.URL)

        self.assertEqual(response.status_code, 200, "ROOT post_success #1")
        self.assertEqual(len(response.data), 3, "ROOT post_success #2")

        response = self.client.post(
            self.URL,
            {
                "username": "test_user4",
                "password1": "test_password",
                "password2": "test_password",
                "name": "Test User 4",
                "email": "test@test.com",
            },
        )
        self.assertEqual(
            response.data["username"], "test_user4", "ROOT post_success #3"
        )
        self.assertEqual(response.data["name"], "Test User 4", "ROOT post_success #4")
        self.assertEqual(
            response.data["email"], "test@test.com", "ROOT post_success #5"
        )
        self.assertIsNone(response.data.get("password"), "ROOT post_success #6")
        self.assertEqual(response.status_code, 201, "ROOT post_success #7")

        # check if user was created
        self.assertEqual(User.objects.count(), 4, "ROOT post_success #8")

    # def test_post_fail_password_not_match(self):
    #     response = self.client.post(
    #         URL,
    #         {
    #             "username": "test_user4",
    #             "password1": "test_password",
    #             "password2": "test_password2",
    #             "name": "Test User 4",
    #             "email": "test@test.com",
    #         },
    #     )

    #     pass


class AuthTestCase(APITestCase):

    URL = f"{BASE_URL}/auth"

    def setUp(self):
        create_user("test_user", "test_password")

    def test_get(self):
        self.client.login(username="test_user", password="test_password")
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200, "AUTH get_success #1")

    def test_get_fail(self):
        self.client.logout()
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 401, "AUTH get_fail #1")
