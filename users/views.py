from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from common import utils
from .models import User
from . import serializers


class ROOT(APIView):

    def get(self, request):
        page = utils.get_page(request)

        # get users per page
        users = utils.get_page_items(page, User.objects.all())
        serializer = serializers.TinyUserSerializer(
            users,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):

        print("POST: /user")
        print(request.data)
        password1 = request.data.get("password1")
        password2 = request.data.get("password2")
        if password1 != password2:
            return Response(
                {"error": "Passwords do not match"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        password = password1

        serializer = serializers.PrivateUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_409_CONFLICT,
            )

        user = serializer.save()
        # set password by calling set_password method for hashing it
        user.set_password(password)
        user.save()
        serializer = serializers.PrivateUserSerializer(user)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class PK(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound("User does not exist")

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)


class Password(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):

        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError("Old password and new password are required")

        if not user.check_password(old_password):
            raise ParseError("Old password is incorrect")

        user.set_password(new_password)
        user.save()
        return Response(status=204)


class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if not user:
            return Response({"error": "wrong password"})

        login(request, user)
        return Response({"ok": "Welcome!"})


class Logout(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "bye!"})


class Me(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = serializers.PrivateUserSerializer(request.user)
        return Response(serializer.data)
