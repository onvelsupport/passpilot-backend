from django.urls import path

from .views import (
    ask_coach,
    examiner_mode,
    explain_wrong_answer,
    generate_similar_questions,
    study_recommendation,
)

urlpatterns = [
    path("ask/", ask_coach, name="ask_coach"),
    path("study-recommendation/", study_recommendation, name="study_recommendation"),
    path("explain-wrong-answer/", explain_wrong_answer, name="explain_wrong_answer"),
    path("similar-questions/", generate_similar_questions, name="similar_questions"),
    path("examiner-mode/", examiner_mode, name="examiner_mode"),
]