from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['sharktanks']
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
for x in d:
    print(str(x[0])+','+str(x[1])+','+str(x[2])+','+str(x[3])+','+str(x[4]))
    csvfile.write(str(x[0])+','+str(x[1])+','+str(x[2])+','+str(x[3])+','+str(x[4])+','+str(x[5])+'\n')
