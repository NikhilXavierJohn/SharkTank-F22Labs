import csv
import json
from pymongo import MongoClient

csvfile = open('data.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient('localhost', 27017) 
db=mongo_client['sharktanks']
db.data.drop()
header= ["Season","No in series","Company","Deal","Industry","Entrepreneur Gender","Amount","Equity","Valuation","Corcoran","Cuban","Greiner","Herjavec","John","O'Leary","Harrington","Guest","# Sharks","Val per shark","Details / Notes"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.data.insert(row)