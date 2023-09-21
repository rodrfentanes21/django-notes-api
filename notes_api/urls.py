from django.urls import path

from notes_api import views

urlpatterns = [
    path('users/', views.UserApiViewRoutes.as_view()),
    path('notes/', views.NotesApiViewRoutes.as_view()),
]