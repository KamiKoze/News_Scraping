import requests, bs4
# import lxml
# from requests_html import HTMLSession


# session = HTMLSession()
URL = "https://ria.ru/20210705/more-1740010917.html"
page = requests.get(URL)
soup = bs4.BeautifulSoup(page.content, "html.parser")
meta_tags = soup.find_all(name="meta")
for item in meta_tags:
    property_value = item.get('property')
    if property_value == 'article:published_time':
        published_time = item.get('content')
    elif property_value == 'article:modified_time':
        modified_time = item.get('content')

# published_dtg = soup.find("span", "article__info-date")
# modified_dtg = soup.find("span", "article__info-date-modified")
title = soup.title
article = soup.find("div", itemprop="articleBody")


class Scraper:

    # def start(self):
    #     self.removeTags()
    #     self._url()
    #     self._title()
    #     self._article()


    # def removeTags(self):
    #     for data in x(['style', 'script']):
    #         data.decompose()
    #     return ' '.join(x.stripped_strings)


    def _url(self):
        print(f"\n{URL}")


    def _publishedTime(self):
        # for data in published_time(['style', 'script']):
        #     data.decompose()
        # print(f"\n{' '.join(published_time.stripped_strings)}")
        # print(f"\n{published_time}")
        publishedTimeList=modified_time.split("T")
        print(f"\n{publishedTimeList[0]}")
        print(f"\n{publishedTimeList[1]}")


    def _modifiedTime(self):
        # for data in modified_time(['style', 'script']):
        #     data.decompose()
        # print(f"\n{' '.join(modified_time.stripped_strings)}")
        # print(f"\n{modified_time.split("t")}")
        modifiedTimeList=modified_time.split("T")
        print(f"\n{modifiedTimeList[0]}")
        print(f"\n{modifiedTimeList[1]}")


    def _title(self):
        for data in title(['style', 'script']):
            data.decompose()
        print(f"\n{' '.join(title.stripped_strings)}")


    def _article(self):
        for data in article(['style', 'script']):
            data.decompose()
        print(f"\n{' '.join(article.stripped_strings)}")



if __name__ == '__main__':
    sc = Scraper()
    # sc.start()
    sc._url()
    sc._publishedTime()
    sc._modifiedTime()
    sc._title()
    sc._article()
# print(f"\n{Scraper._url(URL)}")
# print(f"\n{Scraper._title(title)}")
# print(f"\n{Scraper._article(article)}")


fields = "URL, Title, Article"
table = "table"
conditions = "condition1=1 AND condition2=2"

sql = (f"SELECT {fields} "
       f"FROM {table} "
       f"WHERE {conditions};")

"""Try this later: https://www.scrapingbee.com/blog/crawling-python/"""
