import json
import random

from channels.generic.websocket import WebsocketConsumer
import time

dummy_messages = [
    """
맨발로 기억을 거닐다
떨어지는 낙엽에
그간 잊지 못한 사람들을 보낸다
""",
    """
맨발로 기억을 거닐다
붉게 물든 하늘에
그간 함께 못한 사람들을 올린다
""",
    """
시간은 물 흐르듯이 흘러가고
난 추억이란 댐을 놓아
미처 잡지 못한 기억이 있어
오늘도 수평선 너머를 보는 이유
""",
    """
맨발로 기억을 거닐다
날 애싸는 단풍에
모든 걸 내어주고 살포시 기대본다
""",
    """
맨발로 기억을 거닐다
다 익은 가을내에
허기진 맘을 붙잡고 곤히 잠이 든다
""",
    """
가슴의 꽃과 나무 시들어지고
깊게 묻혀 꺼내지 못할 기억
그 곳에 잠들어 버린
그대로가 아름다운 것이

슬프다 슬프다
""",
    """
맨발로 기억을 거닐다
노란 은행나무에
숨은 나의 옛날 추억을 불러본다
""",
    """
맨발로 기억을 거닐다
불어오는 바람에
가슴으로 감은 눈을 꼭 안아본다
""",
]


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("connect")
        self.accept()
        self.send(text_data=json.dumps({"data": "connected..?"}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print("receive:", message)

        # get random index of dummy_messages
        random_index = random.randint(0, len(dummy_messages) - 1)
        random_message = dummy_messages[random_index]

        print("random_message:", random_message)

        response_message = ""

        for char in random_message:
            response_message += char
            # response message asynchronusly
            self.send(
                text_data=json.dumps({"message": response_message, "pending": True})
            )
            time.sleep(0.1)

        self.send(text_data=json.dumps({"message": response_message, "pending": False}))
