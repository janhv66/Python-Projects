import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        req = urllib.request.Request(self.site, headers = headers)
        html = urllib.request.urlopen(req).read()
        sp = BeautifulSoup(html, "html.parser")
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if not url:
                continue
            if "articles" in url or "/read/" in url:
                if url.startswith("./"):
                    url = "https://news.google.com" + url[1:]
                print(url)

news = "https://news.google.com/"
Scraper(news).scrape()