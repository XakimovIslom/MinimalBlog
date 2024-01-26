from rest_framework.response import Response
from rest_framework.views import APIView

from apps.contact.models import ContactUsRequest, ContactUs
from .serializers import ContactUsRequestSerializer, ContactUsSerializer


class ContactUsRequestAPIView(APIView):
    def get(self, request):
        cur = ContactUsRequest.objects.all()
        data = {
            'cur': ContactUsRequestSerializer(cur, many=True).data
        }
        return Response(data)


class ContactUsAPIView(APIView):
    def get(self, request):
        cur = ContactUs.objects.all()
        data = {
            'cur': ContactUsSerializer(cur, many=True).data
        }
        return Response(data)
