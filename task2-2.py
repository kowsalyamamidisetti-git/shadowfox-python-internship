#python
from urllib.request import urlopen
from html.parser import HTMLParser

class BookScraper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_price = False
        self.titles = []
        self.prices = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "h3":
            self.in_title = True

        if tag == "p" and "price_color" in attrs.get("class", ""):
            self.in_price = True

    def handle_data(self, data):
        if self.in_title and data.strip():
            self.titles.append(data.strip())

        if self.in_price and data.strip():
            self.prices.append(data.strip())

    def handle_endtag(self, tag):
        if tag == "h3":
            self.in_title = False

        if tag == "p":
            self.in_price = False


url = "https://books.toscrape.com/"

try:
    with urlopen(url, timeout=10) as response:
        html = response.read().decode("utf-8")

    scraper = BookScraper()
    scraper.feed(html)

    print("BOOK TITLES AND PRICES\n")

    for title, price in zip(scraper.titles, scraper.prices):
        print("Title:", title)
        print("Price:", price)
        print("-" * 30)

except Exception as error:
    print("Error:", error)
