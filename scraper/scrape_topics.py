from bs4 import BeautifulSoup
import requests


def scrape_topics(url):
    base_url = "https://www.brainyquote.com/"
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        topic_elements = soup.find_all('div', class_='bqLn')

        topics_list = []

        for topic_element in topic_elements:
            topic_link = topic_element.find('a', class_='topicIndexChicklet')
            if topic_link:
                topic_name = topic_link.find('span', class_='topicContentName').text.strip()
                topic_url = base_url + topic_link['href']
                topics_dict = {
                    "topic_name": topic_name,
                    "topic_url": topic_url,
                }
                topics_list.append(topics_dict)

        return topics_list

    except Exception as e:
        print("An error occurred:", e)
        return []
