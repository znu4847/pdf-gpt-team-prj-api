from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class LLMChoices(models.TextChoices):
        OPEN_AI = ("openai", "Open AI")
        CLAUDE = ("claude", "Claude")

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    password = models.CharField(max_length=128, editable=False)
    name = models.CharField(max_length=150, default="", editable=True)
    avatar = models.URLField(blank=True)

    llm_type = models.CharField(
        max_length=20,
        choices=LLMChoices.choices,
        default=LLMChoices.OPEN_AI,
    )

    openai_key = models.CharField(max_length=200, blank=True)
    claude_key = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.username
