import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

with open("products.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # CSV headings
    writer.writerow(["Product Name", "Price", "Availability"])

    products = soup.find_all("article", class_="product_pod")

    for product in products:

        name = product.h3.a["title"]

        price = product.find(
            "p", class_="price_color"
        ).get_text(strip=True)

        availability = product.find(
            "p", class_="instock availability"
        ).get_text(strip=True)

        writer.writerow([
            name,
            price,
            availability
        ])

print("Product information saved to products.csv")
