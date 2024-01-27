from django.urls import path

from apps.blog.views import PostFeaturedAPIView, PostPopularAPIView, PostRecentlyAPIView, CategoryAPIView, TagAPIView, \
    TodaysUpdateAPIView, SearchAPIView, CategoryWithImageAPIView, PostDetailAPIView

urlpatterns = [
    path('post-featured/', PostFeaturedAPIView.as_view()),
    path('post-popular/', PostPopularAPIView.as_view()),
    path('post-recently/', PostRecentlyAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
    path('tag/', TagAPIView.as_view()),
    path('todays-update/', TodaysUpdateAPIView.as_view()),
    path('search/', SearchAPIView.as_view()),
    path('category-image/', CategoryWithImageAPIView.as_view()),
    path('post/<int:pk>/', PostDetailAPIView.as_view()),
]
