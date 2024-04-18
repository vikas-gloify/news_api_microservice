import json

import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.news_functions import fetch_news_from_mongodb_to_postgres

# Create your views here.

class NewsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        try:
            news_data = fetch_news_from_mongodb_to_postgres()
            news_data = [{ key:str(value) if key=='_id' else value for key,value in each_dict.items()} for each_dict in news_data]
            return Response({"data":news_data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
