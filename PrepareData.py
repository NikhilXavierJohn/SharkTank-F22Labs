import csv
import json
from pymongo import MongoClient
mongo_client=MongoClient('localhost', 27017) 
class Preparedata:
    def dump_to_db(self):
        csvfile = open('data.csv', 'r')
        reader = csv.DictReader( csvfile )
        db=mongo_client['sharktanks']
        db.data.drop()
        header= ["Season","No in series","Company","Deal","Industry","Entrepreneur Gender","Amount","Equity","Valuation","Corcoran","Cuban","Greiner","Herjavec","John","O'Leary","Harrington","Guest","# Sharks","Val per shark","Details / Notes"]

        for each in reader:
            row={}
            for field in header:
                row[field]=each[field]

            db.data.insert(row)
        self.mine_from_db()

    def mine_from_db(self):
        db = mongo_client['sharktanks']
        data=db.data.find()
        print(data)
        d=[]

        for x in data:
            investors=[]
            j=list(x.items())
            for i in range(10,17):
                if(j[i][1]=="1"):
                    investors.append(j[i][0])
                investor=('.'.join(investors))
            d.append([j[1][1],j[2][1],j[3][1],j[6][1],investor,j[19][1]])

        csvfile=open('Required.csv','w')
        csvfile.write("Season"+','+"Episode"+','+"Company"+','+"Entrepreneur Gender"+','+"Investor"+','+"Investment_Amount"+'\n')
        for x in d:
            print(str(x[0])+','+str(x[1])+','+str(x[2])+','+str(x[3])+','+str(x[4]))
            csvfile.write(str(x[0])+','+str(x[1])+','+str(x[2])+','+str(x[3])+','+str(x[4])+','+str(x[5])+'\n')
        self.save_to_db()

    def save_to_db(self):
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
p=Preparedata()
p.dump_to_db()