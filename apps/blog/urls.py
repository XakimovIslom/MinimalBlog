from django.urls import path
from .views import CategoryAPIView, TagAPIView, PostAPIView, TagDetailAPIView, CategoryDetailAPIView

urlpatterns = [
    path('post/', PostAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('tag/', TagAPIView.as_view()),
    path('tag/<int:pk>/', TagDetailAPIView.as_view()),
]
