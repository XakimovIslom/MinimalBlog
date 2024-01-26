from django.db import models

from apps.common.models import BaseModel


class ContactUsRequest(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name

class ContactUs(BaseModel):
    content = models.TextField()

    facebook_url = models.CharField(max_length=255)
    twitter_url = models.CharField(max_length=255)
    instagram_url = models.CharField(max_length=255)
    pinterest_url = models.CharField(max_length=255)

    def __str__(self):
        return self.content