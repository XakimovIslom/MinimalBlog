from django.db import models

from apps.common.models import BaseModel
from apps.users.models import Author


class Category(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category/")
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Tag(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Post(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post/")
    short_content = models.CharField(max_length=255)
    content = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts"
    )
    tag = models.ManyToManyField(Tag, related_name="posts")

    published_date = models.DateField(auto_now_add=True)

    read_min = models.CharField(max_length=255)

    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title
