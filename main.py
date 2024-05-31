import os
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
import logging
import time
import threading
from dotenv import load_dotenv

load_dotenv()


logging.basicConfig(filename='scraper.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')


mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['vakil_desk']
collection = db['assignment']


urls = [
    "https://www.scrapethissite.com/pages/ajax-javascript/#2015",
    "https://www.scrapethissite.com/pages/forms/",
    "https://www.scrapethissite.com/pages/advanced/"
]

# webscraping using beautifulsoup
def scrape_and_save(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        
        data = {
            "title": soup.title.string if soup.title else 'No title',
            "text": soup.get_text(),
            "html": str(soup)
        }
        save_to_mongodb(data, url)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error scraping {url}: {e}")


def save_to_mongodb(data, url):
    if data:
        try:
            collection.insert_one({"url": url, "data": data})
            print(f"Data from {url} saved successfully.")
        except Exception as e:
            logging.error(f"Error saving data to MongoDB: {e}")

#using threads for optimisations
def main():
    threads = []
    for url in urls:
        thread = threading.Thread(target=scrape_and_save, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
