import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib.parse
from bson import json_util
import json
import redis

#Redis
r = redis.Redis()

url = "https://www.blockchain.com/btc/unconfirmed-transactions"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options,executable_path='/usr/bin/chromedriver')
driver.get(url)

def webScraper():
    #Scrape the data to a list
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    btcDetails = [html.get_text() for html in soup.find_all("div", attrs={"class": "sc-6nt7oh-0 kduRNF"})]

    #Merge every 4 element in the list together so we get hash+time+amount(btc)+amount(usd) as 1 element in the list
    btcDetails = iter(btcDetails)
    btcTransactionDetails = [f"{btcDetail} {next(btcDetails, ' ')} {next(btcDetails, ' ')} {next(btcDetails, ' ')}" for btcDetail in btcDetails]

    return btcTransactionDetails

while True:
    data = webScraper()

    #Store the data in redis for 60 seconds
    r.set('topBTC', json.dumps(data))
    r.expire('topBTC', 60)

    time.sleep(60)


