from django.urls import path

from notes_api import views

urlpatterns = [
    path('users/', views.UserApiViewRoutes.as_view())
]