

from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.NoteListCreateAPIView.as_view()),
    path('api/<int:pk>', views.NoteDetailAPIView.as_view()),
    path('api/important/', views.ImportantNoteListAPIView.as_view()),
    path('api/public/', views.PublicNoteListAPIView.as_view()),
    path('api/status/', views.StatusNoteListAPIView.as_view()),
]
