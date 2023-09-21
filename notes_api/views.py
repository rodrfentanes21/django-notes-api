from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from notes_api import models
from notes_api import serializers


class UserApiViewRoutes(APIView):
    """App routes that use API View (document what routes belong here later)"""

    allowed_methods = ['GET']

    def get(self, request, format=None):
        """Return a list of all Users"""
        users = models.UserProfile.objects.all()
        serializer = serializers.UserProfileSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)