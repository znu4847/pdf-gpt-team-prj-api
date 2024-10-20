from django.db import models

from common.models import CommonModel


# Create your models here.
class Conversation(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="conversations",
    )
    title = models.CharField(
        max_length=150,
        default="",
    )
    pdf_url = models.URLField(blank=True)
    last_message = models.ForeignKey(
        "chat_messages.Message",
        on_delete=models.SET_NULL,
        related_name="last_message_conversation",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.pk}"
