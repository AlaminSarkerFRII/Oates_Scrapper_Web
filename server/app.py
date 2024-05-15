from fastapi import FastAPI, HTTPException
from database.models import Topics, Quotes
from bson import ObjectId
from database.db_connections import get_mongo_client
from typing import List

app = FastAPI()


#  Get DB connection and database

client = get_mongo_client()

db = client["quotes_db"]



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


# ===========>  get all Topics (Solved) =========>

@app.get("/topics/", response_model=List[Topics])
async def read_all_topics():
    try:
        topics_collection = db["topics"]
        topics = list(topics_collection.find({}))
        if topics:
            return topics
        else:
            raise HTTPException(status_code=404, detail="No topics found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


# ===========>  create Topics ( posted but not saved in db ) =========>

@app.post("/topics/create")
async def create_topic(topics: Topics):
    try:
        inserted_topic = db.topics.insert_one(topics.dict())
        return {"id": str(inserted_topic.inserted_id)}
    except Exception as e:
        print("Error occurred while inserting topic:", e)
        raise HTTPException(status_code=500, detail="Failed to create topic")



# ================> get single topic ( solved )===============>

@app.get("/topics/{topic_id}")
async def read_topic(topic_id: str):
    try:
        topic = db.topics.find_one({"_id": ObjectId(topic_id)})
        if topic:
            topic["_id"] = str(topic["_id"])
            return topic
        else:
            raise HTTPException(status_code=404, detail="Topic not found")
    except Exception as e:
        print("Error occurred while inserting topic:", e)
        raise HTTPException(status_code=500, detail="Failed to create topic")


# =============== update ( Solved ) ============>

@app.put("/topics/{topic_id}")
async def update_topic(topic_id: str, topic: Topics):
    try:    
        existing_topic = db.topics.find_one({"_id": ObjectId(topic_id)})
        if existing_topic:
            db.topics.update_one({"_id": ObjectId(topic_id)}, {"$set": topic.dict()})
            return {"message": "Topic updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Topic not found")   
    except Exception as e:
        print("Error occurred while inserting topic:", e)
        raise HTTPException(status_code=500, detail="Failed to update topic")


# ============== delete topic =================>

@app.delete("/topics/{topic_id}")
async def delete_topic(topic_id: str):
    try:
        result = db.topics.delete_one({"_id": ObjectId(topic_id)})
        if result.deleted_count == 1:
            return {"message": "Topic deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Topic not found")
    except Exception as e:
        print("Error occurred while inserting topic:", e)
        raise HTTPException(status_code=500, detail="Failed to delete topic")



# ============> Quotes API Routes ==============>
# ============> Quotes all (Given Internal error but data comes in terminal ) =====================>

@app.get("/quotes/", response_model=List[Quotes])
async def read_all_quotes():
    try:
        quotes_collection = db["quotes"]
        quotes = list(quotes_collection.find({}))
        for quote in quotes:
            print ("",quote)
            quote["scraped_at"] = quote["scraped_at"].strftime("%Y-%m-%d")
        if quotes:
            return quotes
        else:
            raise HTTPException(status_code=404, detail="No quotes found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


# ============> Quotes create ( solved created but not saved in db)  ==============>

@app.post("/quotes/create/",)
async def create_quote(quote: Quotes):
    try:
        inserted_quote = db.quotes.insert_one(quote.dict())
        return {"id": str(inserted_quote.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


# ================> get single quote ( solved )===============>

@app.get("/quotes/{quote_id}")
async def read_quote(quote_id: str):
    try:  
        quote = db.quotes.find_one({"_id": ObjectId(quote_id)})
        if quote:
            quote["_id"] = str(quote["_id"])
            return quote
        else:
            raise HTTPException(status_code=404, detail="Quote not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


# =================> update quote (solved) =================>

@app.put("/quotes/{quote_id}")
async def update_quote(quote_id: str, quote: Quotes):
    try:
        existing_quote = db.quotes.find_one({"_id": ObjectId(quote_id)})
        if existing_quote:
            db.quotes.update_one({"_id": ObjectId(quote_id)}, {"$set": quote.dict()})
            return {"message": "Quote updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Quote not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


# =================> delete quote =================>

@app.delete("/quotes/{quote_id}")
async def delete_quote(quote_id: str):
    try:
        result = db.quotes.delete_one({"_id": ObjectId(quote_id)})
        if result.deleted_count == 1:
            return {"message": "Quote deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Quote not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
