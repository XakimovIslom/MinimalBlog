from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from apps.users.models import Author
from apps.users.serializers import AuthorSerializer


class AuthorAPIView(APIView):

    def get(self, request):
        posts = Author.objects.all()
        data = {
            'authors': AuthorSerializer(posts, many=True).data
        }
        return Response(data)


# class AuthorListAPIView(ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer