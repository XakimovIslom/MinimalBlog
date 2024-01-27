from django.urls import path

from .views import AuthorTopAPIView, AuthorOurAPIView, AuthorDetailAPIView


urlpatterns = [
    path('', AuthorOurAPIView.as_view()),
    path('top-users/', AuthorTopAPIView.as_view()),
    path('user-detail/<int:pk>/', AuthorDetailAPIView.as_view()),
    # path('user-detail/<int:pk>/', UserPostsAPIView.as_view()),
    # path('user-post/', UserPostsDetailAPIView.as_view()),
]
