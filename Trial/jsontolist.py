#CSV to JSON Conversion
import json
import os

DIR = './static/Data'
dispdata=[]
scount=(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
for s in range(1,scount+1):
    season="season"+str(s)
    seasonfile=season+".json"
    print("reading")
    print(season)
    with open(seasonfile,encoding="utf-8") as data:
        jsondata=data.read()
        datas=json.loads(jsondata)
        # print(datas)
        episodes=len(datas)
        for i in range(1,episodes+1):
            epname="Episode "+str(i)
            companies=len(datas[epname])
            for j in range(companies):
                company=datas[epname][j]
                # print(company['company']['title'])
                companyname=company['company']['title']
                dispdata.append([season,epname,companyname,company['investors']])
