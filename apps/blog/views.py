from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import Category, Tag, Post
from .serializers import CategorySerializer, TagSerializer, PostSerializer


class CategoryAPIView(APIView):

    def get(self, request):
        category = Category.objects.all()
        data = {
            'category': CategorySerializer(category, many=True).data
        }
        return Response(data)


class CategoryDetailAPIView(APIView):

    def get(self, request, pk):

        try:
            category = Category.objects.get(id=pk)
        except:
            return Response({"error": "Object doesnt exist"})

        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):

        try:
            category = Category.objects.get(id=pk)
        except:
            return Response({"error": "Object doesnt exist"})

        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        try:
            category = Category.objects.get(id=pk)
        except:
            return Response({"error": "Object doesnt exist"})

        category = Category.objects.get(id=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagAPIView(APIView):

    def get(self, request):
        tag = Tag.objects.all()
        data = {
            'tag': TagSerializer(tag, many=True).data
        }
        return Response(data)


class TagDetailAPIView(APIView):

    def get(self, request, pk):

        try:
            tag = Tag.objects.get(id=pk)
        except:
            return Response({"error": "Object doesnt exist"})

        tag = Tag.objects.get(id=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def put(self, request, pk):

        try:
            tag = Tag.objects.get(id=pk)
        except:
            return Response({"error": "Object doesnt exist"})

        tag = Tag.objects.get(id=pk)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        try:
            tag = Tag.objects.get(id=pk)
        except:
            return Response({"error": "Object doesnt exist"})
        
        tag = Tag.objects.get(id=pk)
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostAPIView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        post = Post.objects.all()
        category = self.request.query_params.get('category')
        if category:
            post = post.filter(category__title=category)
        tag = self.request.query_params.get('tag')
        if tag:
            post = post.filter(tag__title=tag)
        data = {
            'post': PostSerializer(post, many=True).data
        }
        return Response(data)
