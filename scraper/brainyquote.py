from bs4 import BeautifulSoup
import requests
import time


def scrape_brainyquote_data():
    url = "https://www.brainyquote.com/topics/inspirational-quotes"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # if headers not working -
    # proxies = {
    #     "http": "http://your_proxy_server",
    #     "https": "https://your_proxy_server",
    # }

    try:
        time.sleep(2)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        # for child in soup.descendants:
        #         if child.name:
        #             print(child.name)

        quote_containers = soup.find_all("div", class_="clearfix")
        quotes = []

        for container in quote_containers:
            quote_text = container.find("a", class_="b-qt").text.strip()
            author_name = container.find("a", class_="bq-aut").text.strip()

            # Extract additional information if available (e.g., tags)
            # You can customize this based on the structure of the website
            # additional_info = container.find("span", class_="additional-info").text.strip()

            # Create a dictionary representing the quote

            quote = {
                "text": quote_text,
                "author": author_name,
                # "additional_info": additional_info,
            }

            quotes.append(quote)
            print(quote)
        return quotes
    except Exception as e:
        print("An error occurred:", e)
        return []


if __name__ == "__main__":
    quotes = scrape_brainyquote_data()
    if quotes:
        print("Scraped quotes:", quotes)
    else:
        print("No quotes scraped.")
