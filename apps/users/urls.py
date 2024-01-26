from django.urls import path
from .views import AuthorAPIView

urlpatterns = [
    path('', AuthorAPIView.as_view())
]
