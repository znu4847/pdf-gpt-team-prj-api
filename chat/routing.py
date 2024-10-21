# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(
        r"ws/v1/chat/(?P<user>\w+)/(?P<conversation>\w+)/$",
        consumers.DummyMessageConsumer.as_asgi(),
    ),
]
