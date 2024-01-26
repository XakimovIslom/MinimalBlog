from django.urls import path
from .views import FAQAPIView

urlpatterns = [
    path('', FAQAPIView.as_view())
]
