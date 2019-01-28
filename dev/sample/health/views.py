from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HealthView(APIView):
    """
    Return okay if application is up and running.
    """

    def get(self, request):
        return Response({'Status': 'Active'}, status=status.HTTP_200_OK)


