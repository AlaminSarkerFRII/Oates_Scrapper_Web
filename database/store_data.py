from database.db_connections import get_mongo_client


def store_quotes_in_mongodb(quotes, topics):
    try:
        client = get_mongo_client()
        if client:
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
