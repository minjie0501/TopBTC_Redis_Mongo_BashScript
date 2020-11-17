# TopBTC_Redis_Mongo_BashScript
Bash script:
  1. Installs redis
  2. Installs mongoDB
  3. Runs a python script that scrapes all the BTC transactions from the last minute and adds it to redis (every minute). Redis stores the data for 1 minute.
  4. Runs a python script that fetches the BTC transactions from redis and gets the top 1 transaction, then inserts the top 1 transaction to mongoDB every minute.
