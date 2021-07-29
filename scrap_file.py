import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.startech.com.bd/product/search?&search=gigabyte&limit=20 "
# makes a request to the web page and gets its HTML
page = requests.get(url)
# stores the HTML page in 'soup', a BeautifulSoup object
soup = BeautifulSoup(page.content,  'html.parser')

#print(soup.prettify())
results = soup.find(id="content")
mydivs = results.find_all("div", {"class": "p-item"})

#print(mydivs)

for mydiv in mydivs:
    item_name = mydiv.find("h4", class_="p-item-name")
    #item_image = mydivs.find("img", class_="p-item-img")
    #item_link = mydivs.find('a', href=True, class_="p-item-name")
    item_price = mydiv.find("div", class_="p-item-price")
    print(item_name.text.strip())
    #print(item_image)
    #print(item_link)
    print(item_price.text.strip())
    print()
