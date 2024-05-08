from django.urls import path
from .views import test_view

urlpatterns = [
    path('testing', test_view, name="test"),
]