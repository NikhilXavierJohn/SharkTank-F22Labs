import csv
import json
from pymongo import MongoClient

csvfile = open('Required.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient('localhost', 27017) 
db=mongo_client['F22Labs']
db.data.drop()
header= ["Season","Episode","Company","Entrepreneur Gender","Investor","Investment_Amount"]

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.data.insert(row)