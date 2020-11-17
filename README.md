# TopBTC_Redis_Mongo_BashScript
Bash script:
  1. Installs redis
  2. Installs mongoDB
  3. Runs a python script that scrapes all the BTC transactions from the last minute and adds it to redis (every minute). Redis stores the data for 1 minute.
  4. Runs a python script that fetches the BTC transactions from redis and gets the top 1 transaction, then inserts the top 1 transaction to mongoDB every minute.
  
 
 Prerequisits:

* Python 3.0/3.+
* ChromeDriver
* Python Libraries: selenium, bs4, pandas, numpy, redis, pymongo


How to use:

1. Download the bash and python scripts and make sure to put them in the same folder
1. Open terminal and change the path to where the scripts are located
2. Type 'bash btcStore.sh' in the terminal

