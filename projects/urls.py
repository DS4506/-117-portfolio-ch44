from django.urls import path
from .views import projects_view

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", projects_view, name="projects"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)