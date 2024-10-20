from django.db import models

from common.models import CommonModel


# Create your models here.
class Message(CommonModel):
    class MessageTypeChoices(models.TextChoices):
        SYSTEM_MESSAGE = ("system_message", "System")
        AI_MESSAGE = ("ai_message", "AI")
        HUMAN_MESSAGE = "human_message", "User"

    conversation = models.ForeignKey(
        "chat_conversations.Conversation",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    type = models.CharField(
        max_length=20,
        choices=MessageTypeChoices.choices,
        default=MessageTypeChoices.HUMAN_MESSAGE,
    )
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.conversation}"
