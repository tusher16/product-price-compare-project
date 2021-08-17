from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser


#option = webdriver.ChromeOptions()  ,options=option
#option.add_argument('headless')

driver = webdriver.Chrome('../product-price-compare-project/chromedriver')
driver.get('https://www.ryanscomputers.com/search?q=asus%20monitor')


#players = driver.find_elements_by_xpath('//div[@class="product-content-info"]') 
players = driver.find_elements_by_xpath('//*[@id="hits"]/div/div[1]/div/div[2]/div[1]/a[1]') 

players_list = []

for p in range(len(players)):
    players_list.append(players[p].text)


#salaries = driver.find_elements_by_xpath('//div[@class="price"]')  
salaries = driver.find_elements_by_xpath('//*[@id="hits"]/div/div[1]/div/div[2]/div[1]/div[2]/span')

salaries_list = []

for s in range(len(salaries)):
    salaries_list.append(salaries[s].text)


print(players_list)
print(salaries_list)