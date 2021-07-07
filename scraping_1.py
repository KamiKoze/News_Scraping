import requests
from bs4 import BeautifulSoup
import csv

with open('ria_scraping.csv', mode='w') as ria_scraping:
    ria_scraping = csv.writer(ria_scraping, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    ria_scraping.writerow('URL' 'Title' 'Article')

#URL = "https://ria.ru/"

URL = "https://ria.ru/20210705/more-1740010917.html"
print(URL)

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

title = soup.find("title")
print(title)

article = soup.find("div", itemprop="articleBody")
print(article)

ria_scraping.writerow([URL], [title], [article])
