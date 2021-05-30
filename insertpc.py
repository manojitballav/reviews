import re,time
from pymongo import MongoClient

# calling custom methods
from amazon import *

client = MongoClient('127.0.0.1',27017)
db = client['amazon']
col = db['record']
def dbinsert(data):
    devdata = data
    # print('Data to be inserted')
    name = data[0]
    pc = data[1]
    ram = data[2]
    rom = data[3]
    color = data[4]
    # col.insert_one({'name':name,'asin':pc,'ram':ram,'rom':rom,'color':color})
    if (col.count_documents( { 'asin': pc },limit=1)== 0):
        col.update_one({'asin':pc},{"$set":{'name':name,'asin':pc,'ram':ram,'rom':rom,'color':color}},upsert=True)
        # calling function to initiate data scraping
        # number(devdata)
        return (number(devdata))
    else:
        devdata = (pc +str(' Exists !'))
        return (devdata)
    # print(name,pc,ram,rom,color)

   
    