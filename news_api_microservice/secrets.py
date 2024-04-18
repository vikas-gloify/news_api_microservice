from decouple import config


class Secrets:
    SECRET_KEY = config('SECRET_KEY')

    DATABASE_NAME = config('DATABASE_NAME')
    DATABASE_USER = config('DATABASE_USER')
    DATABASE_PASSWORD = config('DATABASE_PASSWORD')
    DATABASE_HOST = config('DATABASE_HOST')
    DATABASE_PORT = config('DATABASE_PORT')

    # mongo secrets
    MONGO_URL=config('MONGO_URL')
    MONGO_DB=config('MONGO_DB')
    MONGO_COLLECTION=config('MONGO_COLLECTION')

    # newsapi secrets
    NEWSAPI_URL=config("NEWSAPI_URL")
    NEWSAPI_API_KEY=config("NEWSAPI_API_KEY")
    NEWSAPI_DOMAINS=config("NEWSAPI_DOMAINS")
