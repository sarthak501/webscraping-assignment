import os
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
import logging
import time
import threading
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# MongoDB Atlas setup
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['vakil_desk']
collection = db['assignment']

# URLs to scrape
urls = [
    "https://www.scrapethissite.com/pages/ajax-javascript/#2015",
    "https://www.scrapethissite.com/pages/forms/",
    "https://www.scrapethissite.com/pages/advanced/"
]

# Web scraping using BeautifulSoup
def scrape_and_save(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        data = {
            "title": soup.title.string if soup.title else 'No title',
            "text": soup.get_text(),
            "html": str(soup)
        }
        save_to_mongodb(data, url)
        time.sleep(2)  # Sleep to minimize load on the server
    except requests.exceptions.RequestException as e:
        logging.error(f"Error scraping {url}: {e}")

# Save data to MongoDB
def save_to_mongodb(data, url):
    if data:
        try:
            collection.insert_one({"url": url, "data": data})
            print(f"Data from {url} saved successfully.")
        except Exception as e:
            logging.error(f"Error saving data to MongoDB: {e}")

# Using threads for optimization
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
