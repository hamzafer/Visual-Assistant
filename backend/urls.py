from django.urls import path
from backend.views import RecognitionAPIView


urlpatterns = [
    path('image/', RecognitionAPIView.as_view()),
    path('', RecognitionAPIView.home, name='home'),
]
