import logging

from decouple import config
from pymongo.mongo_client import MongoClient

from news_api_microservice.logger import error_log, info_log

from .secrets import Secrets


class MongoConnection:
    def __init__(self,database):
        self.database = database
        self.db = None
        self.connection = None

    def __enter__(self):
        connection_string = Secrets.MONGO_URL
        self.connection = MongoClient(connection_string)
        print(f"list database names:{self.connection.list_database_names()}")
        self.db = self.connection[self.database]
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        self.connection = None
        self.db = None

    def get_collection(self,collection_name):
        return self.db[collection_name]
    

def save_data_to_mongodb(database, collection_name, data, company_literal=None, company_id=None):
    try:
        with MongoConnection(database) as connection:
            collection = connection.get_collection(collection_name)
            data = data.get("articles")
            if company_literal:
                data = [{**d,'company_literal':company_literal, 'company_id':company_id} for d in data]
            if data:
                collection.insert_many(data)
                info_log.info(f"data stored in {database}:{collection_name}")
            else:
                info_log.info(f"No data to store in {database}:{collection_name}")
    except Exception as e:
        error_log.error(f'Error in saving data to mongodb: {str(e)}')

def read_data_from_mongodb(database, collection_name):
    try:
        with MongoConnection(database) as connection:
            collection = connection.get_collection(collection_name)
            data = collection.find()
            if data:
                info_log.info(f"data fetched from {database}:{collection_name}")
                return list(data)
            else:
                info_log.info(f"No data to fetch from {database}:{collection_name}")
                return []
        
    except Exception as e:
        error_log.error(f'Error in reading data from mongodb: {str(e)}')
        return []