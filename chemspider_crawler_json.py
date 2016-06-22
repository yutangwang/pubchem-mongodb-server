"""
Script to build json file from Chemspider

"""
import json
from chemspipy import ChemSpider
import random
from time import gmtime, strftime, sleep

cs = ChemSpider('6a4cb931-b018-4ffe-96e4-85f704e5f2a6')

contributor = input("Enter your name: ")
x = int(input("Enter the first csid to start: "))
y = int(input("Enter the second csid to end: "))

csids = list(range(x, y))
random.shuffle(csids)

doc = {'Contributor': str(contributor)}
dt = strftime("%Y-%m-%d\t%H:%M:%S" , gmtime())
doc['date'] = dt
with open('chemspiderdb.json', 'w') as jsonfile:
    json.dump(doc, jsonfile)
doc = {}

for csid in csids:
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
        print("{0}, Thank you very much!".format(str(contributor)))
        with open('chemspiderdb.json', 'a') as jsonfile:
            json.dump(doc, jsonfile)
    except Exception as e:
        print(str(e) + 'Invalid ID  is ' + str(compound.csid))
        with open('Invalid_ID.txt', 'a') as invalid_id:
            invalid_id.write(str(compound.csid) + '\n')
        continue