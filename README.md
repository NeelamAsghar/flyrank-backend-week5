FlyRank Backend - Week 5 Assignment

Web Scraper with Responsible Scraping

Goal

Build a web scraper that collects data from a practice website, extracts useful information, cleans the data, and stores it in a structured JSON format while following responsible scraping practices.

---

Features

- Scrapes book data from the Books to Scrape practice website.
- Extracts:
  - Book Title
  - Book Price
- Stores the extracted data in a JSON file.
- Scrapes multiple pages automatically.
- Uses a custom User-Agent.
- Implements 2-second rate limiting between requests.
- Checks the website's robots.txt before scraping.

---

Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- JSON
- Time

---

Project Structure

flyrank-backend-week5/
│── data/
│   └── books.json
│── main.py
│── requirements.txt
└── README.md

---

Installation

Clone the repository:

git clone <repository-url>

Move into the project directory:

cd flyrank-backend-week5

Install the required packages:

pip install -r requirements.txt

---

Run the Project

python main.py

---

Output

The scraper creates:

data/books.json

Each record contains:

{
    "title": "Book Title",
    "price": "£51.77"
}

---

Responsible Scraping

- Verified the website's "robots.txt".
- Used a custom "User-Agent" for identification.
- Added a 2-second delay between requests to avoid overloading the server.
- Scraped data only from the practice website provided for educational purposes.

---

Learning Outcomes

Through this assignment, I learned how to:

- Fetch web pages using Requests.
- Parse HTML using BeautifulSoup.
- Extract and clean structured data.
- Save data as JSON.
- Implement responsible web scraping practices, including User-Agent identification, rate limiting, and checking robots.txt.

---

Author

Neelam Asghar

## Output Statement
![Scraper Output](c:\Users\HP ELITE\OneDrive\Desktop\output.png)