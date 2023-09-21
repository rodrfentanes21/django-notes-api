from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from notes_api import models


class ApiViewRoutes(APIView):
    """App routes that use API View (document what routes belong here later)"""
