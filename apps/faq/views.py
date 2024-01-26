from rest_framework.response import Response
from rest_framework.views import APIView

from apps.faq.models import FAQ
from .serializers import FAQSerializer


class FAQAPIView(APIView):

    def get(self, request):
        faq = FAQ.objects.all()
        data = {
            'faq': FAQSerializer(faq, many=True).data
        }
        return Response(data)
