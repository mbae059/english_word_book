from django.urls import path, include
from .views import DayAPIView
urlpatterns = [
    path('', DayAPIView.as_view()),
]
