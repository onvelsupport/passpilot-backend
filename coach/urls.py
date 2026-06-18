from django.urls import path
from .views import CoachView

urlpatterns = [
    path('ask/', CoachView.as_view()),
]