# chat/consumers.py
from email import message
import json
import random
import time

from channels.generic.websocket import WebsocketConsumer

big_big_message = """
맨발로 기억을 거닐다
붉게 물든 하늘에
그간 함께 못한 사람들을 올린다
"""

spec_1 = """
# Conversations UI:
- 로그인 한 유저에게 대화 기록을 보여주세요.
- 유저는 이전 대화를 이어 진행하거나 새로운 대화를 시작할 수 있어야 합니다.
"""

spec_2 = """
# Create Conversation UI:
- 유저가 PDF를 업로드하고 대화에 제목을 붙일 수 있는 Form을 만드세요.
- Langchain을 사용하여 업로드된 PDF를 임베딩하고, 비용 절감을 위해 임베딩을 캐시하세요.
"""

spec_3 = """
# Conversation UI:
- LCEL을 사용해 메모리가 있는 체인을 구현하고, PDF에 대한 질문에 답할 수 있는 기능을 만듭니다.
- 챗봇 UI를 구축하세요.
- LLM의 응답을 스트리밍하세요.
- 메시지와 대화를 파일 정보와 함께 Django 서버에 저장하세요.
- 파일 업로드에 대한 자세한 내용은 에어비앤비 클론코딩 강의의 #11.15 ~ 16를 참고하세요.
"""

spec_4 = """
# Backend Requirements:
- 유저와 챗봇 간의 대화를 저장하기 위한 Conversation 모델과 Message 모델을 만드세요.
- 각 Conversation은 User에 대한 외래키(Foreign Key)를 가져야 합니다.
- 각 Message는 Conversation에 대한 외래키(Foreign Key)를 가져야 합니다.
- 새로운 대화를 생성하고 로그인한 유저의 모든 대화를 볼 수 있는 DRF 기반의 /api/v1/conversations/... 엔드포인트를 구축하세요.
- 대화의 메시지 기록을 가져오고 대화에 새 메시지를 추가하기 위한 DRF 기반의 /api/v1/messages/... 엔드포인트를 구축하세요.
"""


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(f"receive{message}")
        self.send(text_data=json.dumps({"message": message}))


class DummyMessageConsumer(WebsocketConsumer):
    def connect(self):
        print("--- connect ---")
        print("---------------")
        print(self.scope["query_string"].decode())
        print("---------------")
        # token = self.scope['query_string'].decode().split('=')[1]
        # token = self.scope['query_string'].decode().split('=')[1]

        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # random number between 1 and 3
        random_number = random.randint(1, 3)
        messages = [spec_1, spec_2, spec_3, spec_4]
        message = messages[random_number]

        # devide big_message by character and send every 0.01 second
        for i in range(len(message)):
            self.send(
                text_data=json.dumps(
                    {
                        "message": message[0:i],
                        "pending": True,
                    }
                )
            )
            time.sleep(0.01)

        # send done message
        self.send(text_data=json.dumps({"message": "", "pending": False}))
