from flask import Flask, render_template,request,jsonify
from pymongo import MongoClient
import os
import json
from flask_restplus import reqparse

app = Flask (__name__)
client = MongoClient('localhost', 27017)
db = client['F22Labs']
app = Flask(__name__)


datas=[]    
filters=['Season','Episode','Gender','Investor']
dic={}
parser = reqparse.RequestParser()
@app.route("/")
def index():
    data=db.data.find()
    for x in data:
        j=list(x.items())
        datas.append([j[1][1],j[2][1],j[3][1],j[4][1],j[5][1],j[6][1]])
    return render_template('index.html', data=datas)
@app.route("/company/",methods=['GET'])
def company():
    x=request.args.get('compname')
    print(type(x))
    DIR = './static/Data'
    dispdata=[]
    scount=(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
    for s in range(1,scount+1):
        season="season"+str(s)
        seasonfile=season+".json"
        with open(DIR+'/'+seasonfile,encoding="utf-8") as data:
            jsondata=data.read()
            datas=json.loads(jsondata)
            episodes=len(datas)
            for i in range(1,episodes+1):
                epname="Episode "+str(i)
                companies=len(datas[epname])
                for j in range(companies):
                    company=datas[epname][j]
                    companyname=company['company']['title']
                    try:
                        links=company['company']['link']
                    except:
                        links=""
                    status=company['status']
                    investment=company['kitna']
                    socialmedia=company['social']
                    product=company['product']
                    
                    if(x==companyname):
                        dispdata.append([season,epname,companyname,links,socialmedia,product,company['investors'],investment,status])
                        print(x)
                        print("this works")
    print(dispdata)
    return render_template('Company.html', data=dispdata)

@app.route("/filter/",methods=['GET'])
def filter():
    command=None
    for i in filters:
        x=parser.add_argument(i, action='append')
        x=dict(parser.parse_args())
    for i in x:
        c=x.get(i)
        if(c!=None):
            dic[i]=c
    print(dic)
    datas=[]
    if(dic!={}):
        length=len(dic)
        print(length)
        if(length<2):
            command="{'$or':["
            for i in dic:
                sublength=len(dic.get(i))
                for j in range(sublength):
                    command=command+"{"+(dic.get(i)[j])+"},"
            command=command+"]}"
            print(command)
            data=db.data.find(eval(command))
            for x in data:
                j=list(x.items())
                datas.append([j[1][1],j[2][1],j[3][1],j[4][1],j[5][1],j[6][1]])
        else:
            sub=[]
            command="{'$and':["
            
            for i in dic:
                subcommand="{'$or':["
                sublength=len(dic.get(i))
                for j in range(sublength):
                    subcommand=subcommand+"{"+(dic.get(i)[j])+"},"
                subcommand=subcommand+"]}"
                sub.append(subcommand)

            for i in range(len(sub)):
                command=command+sub[i]+','
            command=command+"]}"
            print(command)
            data=db.data.find(eval(command))
            for x in data:
                j=list(x.items())
                datas.append([j[1][1],j[2][1],j[3][1],j[4][1],j[5][1],j[6][1]])

    return render_template('index.html', data=datas)
if __name__ == "__main__":
    app.run(debug=True)
