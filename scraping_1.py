import requests
from bs4 import BeautifulSoup

URL = "https://ria.ru/20210705/more-1740010917.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

class Scraper:

    def start(self):
        self._url()
        self._title()
        self._article()

    def _url(self):
        print(URL)

    def _title(self):
        title = soup.find("title")
        print(title)

    # def _description(self):
    #     print(description)

    def _article(self):
        article = soup.find("div", itemprop="articleBody")
        print(article)

if __name__ == '__main__':
    sc = Scraper()
    sc.start()
