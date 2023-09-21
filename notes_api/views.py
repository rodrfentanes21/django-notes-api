from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from notes_api import models
from notes_api import serializers


class UserApiViewRoutes(APIView):
    """User related routes that use API View (document what routes belong here later)"""

    allowed_methods = ['GET']

    def get(self, request, format=None):
        """Return a list of all Users"""
        users = models.UserProfile.objects.all()
        serializer = serializers.UserProfileSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class NotesApiViewRoutes(APIView):
    """Note related routes that use API View (document what routes belong here later)"""

    allowed_methods = ['GET', 'POST']

    def get(self, request, format=None):
        """Return a list of all Users"""
        notes = models.Note.objects.all()
        serializer = serializers.NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        """Create and return a new note"""
        title = request.data.get('title')
        body = request.data.get('body')
        serializer = serializers.NotesSerializer(data={'title': title, 'body': body})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)