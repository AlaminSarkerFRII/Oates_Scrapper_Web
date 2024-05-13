import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def store_quotes_in_mongodb(quotes, topics):
    try:
        username = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        connection_string = f"mongodb+srv://{username}:{password}@cluster1.nmlgnvj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

        client = MongoClient(connection_string)
        db = client["quotes_db"]
        if topics:
            collection = db["topics"]
            result = collection.insert_many(topics)
        elif quotes:
            collection = db["quotes"]
            result = collection.insert_many(quotes)
        else:
            print("No quotes or topics to store.")
            return
        print("Inserted IDs:", result.inserted_ids)

    except Exception as e:
        print("An error occurred while storing quotes in MongoDB:", e)
