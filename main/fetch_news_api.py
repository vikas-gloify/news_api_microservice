from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main.news_functions import fetch_news_from_newsapi
from news_api_microservice.logger import error_log, info_log


class FetchnewsView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            info_log.info("Fetch news from newsapi")
            company_details = request.data['company_details']
            fetch_news_from_newsapi(company_details=company_details)
            info_log.info("Fetchnews initiated successfully")
            return Response({"message": "News is being fetched!"}, status=status.HTTP_200_OK)
        except Exception as e:
            error_log.error(f"Error in fetching news from newsapi: {str(e)}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
