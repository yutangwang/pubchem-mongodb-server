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

csids = list(range(2501, 5001))
random.shuffle(csids)
doc = {}

for csid in csids:
    se = chemspider.find_one({'_id': csid})
    if se is not None:
        continue
    compound = cs.get_compound(csid)
    try:
        doc['_id'] = int(compound.csid)
        doc['common_name'] = compound.common_name
        sleep(random.uniform(0.2, 1.2))
        doc['molecular_weight'] = compound.molecular_weight
        sleep(random.uniform(0.2, 1.2))
        doc['molecular_formula'] = compound.molecular_formula
        doc['stdinchi'] = compound.stdinchi
        sleep(random.uniform(0.2, 1.2))
        doc['stdinchikey'] = compound.stdinchikey
        doc['smiles'] = compound.smiles
        sleep(random.uniform(1, 3))
    except Exception as e:
        print(str(e) + 'Invalid ID  is ' + str(compound.csid))
        with open('Invalid_ID.txt', 'a') as invalid_id:
            invalid_id.write(str(compound.csid) + '\n')
    try:
        chemspider.insert_one(doc)
    except Exception as e:
        print(str(e) + "data insert error" + str(csid)+ '\n')
        with open('mongodb_server_log.txt', 'w') as mongo_error_log:
            mongo_error_log.write(strftime("%Y-%m-%d\t%H:%M:%S" + "---cisd " + str(doc['_id']) + 'insert error \n', gmtime()))