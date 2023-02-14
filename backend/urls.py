from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('word/', include('Word.urls')),
    path('day/', include('Day.urls')),
    path('image/', include('Image.urls')),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)