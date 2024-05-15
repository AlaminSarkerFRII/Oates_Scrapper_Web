from scraper.scrape_quotes import scrape_quotes_from_topic
from scraper.scrape_topics import scrape_topics
from database.store_data import store_quotes_in_mongodb


def scrape_brainyquote_data():
    base_url = "https://www.brainyquote.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        topics = scrape_topics(base_url + "topics")
        # store_quotes_in_mongodb(topics)

        all_quotes = []

        for topic in topics:
            topic_url = topic["topic_url"]
            quotes = scrape_quotes_from_topic(topic_url, headers)
            all_quotes.extend(quotes)

        return [all_quotes, topics]

    except Exception as e:
        print("An error occurred during scraping:", e)
        return []


if __name__ == "__main__":
    quotes, topics = scrape_brainyquote_data()
    if quotes or topics:
        store_quotes_in_mongodb(quotes, topics)
        print("Scraped and stored quotes successfully.")
    else:
        print("No quotes scraped.")
