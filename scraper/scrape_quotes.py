from datetime import datetime
from bs4 import BeautifulSoup
import requests


def scrape_quotes_from_topic(topic_url, headers):
    try:
        response = requests.get(topic_url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        quote_containers = soup.find_all("div", class_="clearfix")
        quotes_list = []

        for container in quote_containers:
            quote_text = container.find("a", class_="b-qt").text.strip()
            author_name = container.find("a", class_="bq-aut").text.strip()

            quote = {
                "quote_text": quote_text,
                "author_name": author_name,
                "topic_url": topic_url,
                "scraped_at": datetime.now()
            }
            quotes_list.append(quote)

        return quotes_list

    except Exception as e:
        print("An error occurred while scraping quotes:", e)
        return []
