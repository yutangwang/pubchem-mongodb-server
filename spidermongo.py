"""
Script to build mongodb from Chemspider

"""

from pymongo import MongoClient
from chemspipy import ChemSpider
import random
from time import gmtime, strftime, sleep

client = MongoClient('localhost', 27017)
db = client.mydb
chemspider = db.chemspider

cs = ChemSpider('0064dc77-e5cb-4e86-93da-e8aedd62baa0')


x = int(input("Enter the first csid to start: "))
y = int(input("Enter the second csid to end: "))
csids = [x,y]
with open('retrieving_log.txt', 'a') as retrieving_log:
    retrieving_log.write(strftime("%Y-%m-%d\t%H:%M:%S" , gmtime()))
    retrieving_log.write(strftime('From ' + str(x) + ' to ' + str(y))
#csids = list(range(30001, 40001))
random.shuffle(csids)
doc = {}

for csid in csids:
    se = chemspider.find_one({'_id': csid})
    if se is not None:
        print('{0} has in the mongoDB'.format(str(csid)))
        continue
    compound = cs.get_compound(csid)
    try:
        doc['_id'] = int(compound.csid)
        doc['common_name'] = compound.common_name
        sleep(random.uniform(0.2, 1.2))
        doc['molecular_weight'] = compound.molecular_weight
        sleep(random.uniform(0, 1.2))
        doc['molecular_formula'] = compound.molecular_formula
        doc['stdinchi'] = compound.stdinchi
        sleep(random.uniform(0, 1.2))
        doc['stdinchikey'] = compound.stdinchikey
        doc['smiles'] = compound.smiles
        sleep(random.uniform(1, 1.2))
    except Exception as e:
        print(str(e) + 'Invalid ID  is ' + str(compound.csid))
        with open('Invalid_ID.txt', 'a') as invalid_id:
            invalid_id.write(str(compound.csid) + '\n')
        continue
    try:
        chemspider.insert_one(doc)
        print('{0} has been inserted'.format(str(compound.csid)))
    except Exception as e:
        print(str(e) + "data insert error" + str(csid)+ '\n')
        with open('mongodb_server_log.txt', 'a') as mongo_error_log:
            mongo_error_log.write(strftime("%Y-%m-%d\t%H:%M:%S" + "---cisd " + str(doc['_id']) + 'insert error \n', gmtime()))