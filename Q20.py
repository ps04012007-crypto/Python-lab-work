import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("NEWS HEADLINES AND HYPERLINKS")
print("--------------------------------")

for link in soup.find_all("a"):
    headline = link.get_text(strip=True)
    href = link.get("href")

    if headline and href:
        print("Headline:", headline)
        print("Link:", href)
        print()