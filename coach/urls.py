from django.urls import path
from .views import ask_coach

urlpatterns = [
    path("ask/", ask_coach, name="ask_coach"),
]