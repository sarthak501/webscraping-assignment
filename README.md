# webscraping-assignment


This project is a web scraper that extracts data from specified URLs and stores it in a MongoDB database.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.x
- You have a MongoDB Atlas account and a cluster set up

## Setup Instructions

### Step 1: Clone the Repository

1. Open your terminal or command prompt.
2. Clone the repository by running the following command:

   ```bash
   git clone <your_github_repo_url>


Navigate into the project directory:
cd <repository_name>

# Step 2: Set Up Environment Variables
Create a .env file in the root directory of the project.

Copy the content of .env.example to .env:

Open the .env file in a text editor and replace the placeholder with your actual MongoDB Atlas connection string:

MONGO_URI=your_mongodb_atlas_connection_string


# Step 3: Install Dependencies
Ensure you are in the project directory.

Install the required dependencies by running:
pip install -r requirements.txt


# Step4: Run the Scraper
Run the scraper script by executing:
- python main.py


# Project Structure
- main.py: The main script that performs web scraping and saves data to MongoDB.
- requirements.txt: Lists all the dependencies required for the project.
- .gitignore: Specifies which files and directories to ignore in version control.
- .env.example: An example environment variables file.


# Features
- Robust Data Extraction: The scraper extracts various types of data from web pages, including titles, text, HTML, and structured data like tables.
- Multithreading: Utilizes multithreading to scrape multiple URLs concurrently, enhancing performance and efficiency.
- Error Handling: Comprehensive error handling and logging to manage request failures and parsing errors.
- Graceful Shutdown: Ensures threads complete their tasks before the script exits.


