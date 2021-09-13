import requests
from bs4 import BeautifulSoup
#from requests_html import HTMLSession
#s = HTMLSession()

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"
session = requests.Session()
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE

url = "https://www.techlandbd.com/index.php?route=product/search&search=gigabyte%20monitor "
# makes a request to the web page and gets its HTML

page = session.get(url)
# stores the HTML page in 'soup', a BeautifulSoup object
soup = BeautifulSoup(page.content,  'html.parser')

#print(soup.prettify())
results = soup.find(id="content")
mydivs = results.find_all("div", {"class": "main-products product-grid"})

#print(mydivs)


for mydiv in mydivs:
    item_name = mydiv.find("a", class_="name")
    #item_images = mydiv.find("img-responsive").get('src')
    #item_links = mydiv.find("a").get('href')
    #item_price = mydiv.find("div", class_="price-new")
    print(item_name.text.strip())
    #print(item_images)
    #print(item_links)
    #print(item_price.text.strip())
    print()
