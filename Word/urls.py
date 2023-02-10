from django.urls import path
from .views import WordAPIView
urlpatterns = [
    path('', WordAPIView.as_view()), #post word
    path('<int:id>/', WordAPIView.as_view()), #get word by day
]
