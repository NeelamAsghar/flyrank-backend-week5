import requests
from bs4 import BeautifulSoup
import json
import time

headers = {
    "User-Agent": "FlyRank-Week5-Bot/1.0 (Educational Project)"
}

book_list = []

for page in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Could not access page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        book_list.append({
            "title": title,
            "price": price
        })

    print(f"Page {page} scraped successfully.")
    time.sleep(2)

with open("data/books.json", "w", encoding="utf-8") as file:
    json.dump(book_list, file, indent=4, ensure_ascii=False)

print(f"\nData saved successfully! Total books: {len(book_list)}")