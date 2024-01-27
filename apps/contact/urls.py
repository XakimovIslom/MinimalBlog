from django.urls import path
from .views import ContactUsRequestAPIView, ContactUsAPIView

urlpatterns = [
    path('contact-us-request/', ContactUsRequestAPIView.as_view()),
    path('contact-us/', ContactUsAPIView.as_view()),
]
