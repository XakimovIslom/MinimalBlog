from django.db import models

from apps.common.models import BaseModel


class Author(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="author/")
    description = models.TextField()
    content = models.TextField()

    facebook_url = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    instagram_url = models.CharField(max_length=255)
    pinterest_url = models.CharField(max_length=255)

    is_top = models.BooleanField(default=False)

    def __str__(self):
        return self.title
