from django.db import models

from apps.common.models import BaseModel


class FAQ(BaseModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
