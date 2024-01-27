from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.users.models import Author
from apps.users.serializers import AuthorTopSerializer, AuthorSerializer, AuthorPostDetailSerializer


class AuthorTopAPIView(ListAPIView):
    queryset = Author.objects.filter(is_top=True)
    serializer_class = AuthorTopSerializer


class AuthorOurAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorPostDetailSerializer
