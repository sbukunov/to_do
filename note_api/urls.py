

from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.NoteListCreateAPIView.as_view()),
    path('api/<int:pk>', views.NoteDetailAPIView.as_view()),
    path('api/important/', views.ImportantNoteListAPIView.as_view()),
    path('api/public/', views.PublicNoteListAPIView.as_view()),
    path('api/active/', views.ActiveNoteListAPIView.as_view()),
    path('api/hold/', views.HoldNoteListAPIView.as_view()),
    path('api/done/', views.DoneNoteListAPIView.as_view()),
]
