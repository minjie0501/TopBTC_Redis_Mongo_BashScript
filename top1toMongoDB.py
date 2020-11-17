import pandas as pd
import numpy as np
import time
import urllib.parse
from bson import json_util
import json
import redis
from pymongo import MongoClient

#Connecting to MongoDB
username = urllib.parse.quote_plus('superuser')
password = urllib.parse.quote_plus('p@ss')
client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

#Creating a database called btcDB and a collection called BTC
btcDB = client['btcDB']
col_btc = btcDB['BTC']
    

#Redis
r = redis.Redis()

while True:
    #Fetch the data from redis
    data_fetch = json.loads(r.get('topBTC'))

    address = [i.split()[0] for i in data_fetch]
    times = [i.split()[1] for i in data_fetch]
    amount = [float(i.split()[2]) for i in data_fetch]
    price = [i.split()[4] for i in data_fetch]

    df = pd.DataFrame(list(zip(address,times,amount,price)),columns = ["Hash", "Time", "Amount in BTC", "Amount in USD"])
    df.drop_duplicates(subset=['Hash'])

    #Insert top 1 transaction into mongoDB
    top1 = df.sort_values(by=['Amount in BTC'],ascending=False).head(1).iloc[0]
    col_btc.insert_one(top1.to_dict())
    print(df.sort_values(by=['Amount in BTC'],ascending=False).head(1))

    time.sleep(60)