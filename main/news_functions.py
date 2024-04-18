import logging
from datetime import date, datetime, timedelta
from urllib.parse import urlencode

import requests

from main.models.company_models import Company
from news_api_microservice.logger import error_log, info_log
from news_api_microservice.mongo_conn import (
    read_data_from_mongodb,
    save_data_to_mongodb,
)
from news_api_microservice.secrets import Secrets


def fetch_news_from_newsapi(*args, **kwargs):
    # fetch news from news API
    info_log.info("Fetch news from newsapi")
    company_details = kwargs.pop('company_details')
    try:

        if not company_details:
            info_log.info(f"No company details found")
            return
        
        if not isinstance(company_details, (list, tuple)):
            company_details = list(company_details)
        

        api_url = Secrets.NEWSAPI_URL
        company_literals = "hdfc"
        current_date = datetime.now().date()
        previous_date = datetime.now().date() - timedelta(days=1)
        info_log.info(f"Fetching news from newsapi for {len(company_details)} companies")
        params = {
            "from": previous_date,
            "to": current_date,
            "sortBy": "popularity",
            "apiKey": Secrets.NEWSAPI_API_KEY,
            "domains": Secrets.NEWSAPI_DOMAINS,
            "q": company_literals,
            "language": "en",
            "searchIn": "title,description",
        }

        # updating company literals for each company
        for company in company_details:
            company_literals = " ".join(company["name"].split(" ")[:-1]) if len(company["name"].split(" "))>1 else company["name"]
            params["q"] = company_literals
            encoded_params = urlencode(params)
            full_url = f"{api_url}?{encoded_params}"
            response = requests.get(url=full_url)
            if response.status_code == 200:
                response_data = response.json()
                info_log.info(f"News fetched from newsapi: {len(response_data)}")
                save_data_to_mongodb(
                    database=Secrets.MONGO_DB,
                    collection_name=Secrets.MONGO_COLLECTION,
                    data=response_data,
                    company_literal=company_literals,
                    company_id=company['id']
                )

            else:
                error_log.error(
                    f"Error in fetching news from newsapi: {str(response.status_code)}"
                )

    except Exception as e:
        error_log.error(f"Error in fetching news from newsapi: {str(e)}")

def fetch_news_from_mongodb_to_postgres():
    try:
        news_data_from_mongo = read_data_from_mongodb(Secrets.MONGO_DB, Secrets.MONGO_COLLECTION)
        if news_data_from_mongo:
            return news_data_from_mongo
        else:
            info_log.info(f"No news data to fetch from mongodb to postgres")
            return []
        
    except Exception as e:
        error_log.error(f"Error in fetching news from mongodb to postgres: {str(e)}")