import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def get_mongo_client():
    try:
        username = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        connection_string = f"mongodb+srv://{username}:{password}@cluster1.nmlgnvj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
        client = MongoClient(connection_string)
        return client
    except Exception as e:
        print("An error occurred while establishing MongoDB connection:", e)
        return None
