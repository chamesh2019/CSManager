from django.urls import path

from .views import DocumentView, ModuleView, QuestionsView, AddDocumentView

urlpatterns = [
    path('documents/', DocumentView.as_view()),
    path('modules/', ModuleView.as_view()),
    path('generate_question/', QuestionsView.as_view()),
    path('add_document/', AddDocumentView.as_view())
]