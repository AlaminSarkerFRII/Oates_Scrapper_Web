from pydantic import BaseModel, Field
from datetime import datetime


class Topics(BaseModel):
    topic_name: str
    topic_url: str


class TopicsSchema(BaseModel):
    topic_name: str = Field(..., description="Name of the topic")
    topic_url: str = Field(..., description="URL of the topic")

    class Config:
        schema_extra = {
            "example": {
                "topic_name": "topic_name",
                "topic_url": "topic_url",
            }
        }


class Quotes(BaseModel):
    quote_text: str
    author_name: str
    topic_url: str
    scraped_at: str


class QuotesSchema(BaseModel):
    quote_text: str = Field(..., description="quote_text of the quote")
    author_name: str = Field(..., description="author_name of the quote")
    topic_url: str = Field(..., description="topic_url of the quote")
    scraped_at: str = Field(..., description="scraped_at of the quote")

    class Config:
        schema_extra = {
            "example": {
                "quote_text": "quote_text",
                "author_name": "author_name",
                "topic_url": "topic_url",
                "scraped_at": "scraped_at",
            }
        }
