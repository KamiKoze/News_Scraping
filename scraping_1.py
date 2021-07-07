import requests
from bs4 import BeautifulSoup

#URL = "https://ria.ru/"

URL = "https://ria.ru/20210705/more-1740010917.html"

page= requests.get(URL)

# =============================================================================
# Output to Console
# =============================================================================

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("div", itemprop="articleBody")

#job elements = results.find_all("div", class="schema_org")

print(results)