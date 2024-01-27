from django.db.models import Sum, Q
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Tag, Post
from .serializers import CategorySerializer, TagSerializer, PostPopularSerializer, PostFeaturedSerializer, \
    PostRecentlySerializer, SearchSerializer, CategoryWithImageSerializer, PostDetailSerializer
from ..users.models import Author


class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all().order_by('?')[:5]
    serializer_class = CategorySerializer


class TagAPIView(ListAPIView):
    queryset = Tag.objects.all().order_by()[:9]
    serializer_class = TagSerializer


class PostFeaturedAPIView(ListAPIView):
    queryset = Post.objects.filter(is_featured=True).order_by('?')[:2]
    serializer_class = PostFeaturedSerializer


class PostPopularAPIView(ListAPIView):
    queryset = Post.objects.filter(is_popular=True).order_by("?")[:2]
    serializer_class = PostPopularSerializer


class PostRecentlyAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')[:9]
    serializer_class = PostRecentlySerializer
    pagination_class = LimitOffsetPagination


class TodaysUpdateAPIView(APIView):

    def get(self, request):
        post = Post.objects.all()
        author = Author.objects.all()
        min_read_value = Post.objects.aggregate(blog_read=Sum('read_min'))
        return Response({
            "new_posts": post.count(),
            "total_visitors": author.count(),
            "blog_read": min_read_value,
        })


class SearchAPIView(ListAPIView):
    serializer_class = SearchSerializer

    def get_queryset(self):
        qs = Post.objects.all()
        q = self.request.query_params.get('q')
        if q:
            qs = qs.filter(Q(title__exact=q) | Q(category__title__exact=q) | Q(tag__title__exact=q)).distinct()
        return qs


class CategoryWithImageAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWithImageSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
