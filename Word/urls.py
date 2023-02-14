from django.urls import path
from .views import WordAPIView
urlpatterns = [
    path('', WordAPIView.as_view()), #post word

    #get word by day. Used by CreateWord.js
    path('<int:id>/', WordAPIView.as_view()), 
]
