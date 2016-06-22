import json
from chemspipy import ChemSpider
import random
from time import sleep
import os


if os.path.isfile('idrangeabc.json'):
    with open('idrangeabc.json', 'r') as idrangefile:
        idr = idrangefile.readline()
        idrange = json.loads(idr)
        csids = list(range(idrange['csidfrom'], idrange['csidto']))
        random.shuffle(csids)
        #print(csids)
else:
    print("You need a file named idrangeabc.json. Please send email to wangyt@neau.edu.cn. Thanks!")
    exit()


cs_security_key = ['6a4cb931-b018-4ffe-96e4-85f704e5f2a6','0064dc77-e5cb-4e86-93da-e8aedd62baa0', '66aed41a-8c86-46ac-a75b-8c36db733768','704484fb-3aa5-45f1-b6e1-faaf8aba47af']
'''
cskey = random.choice(cs_security_key)
cs = ChemSpider(cskey)
'''
if os.path.isfile('chemspiderdb.json'):
    spiderjsonfileid = []
    with open('chemspiderdb.json', 'r') as jsonfile:
        for f in jsonfile.readlines():
            the_dict = json.loads(f)
            spiderjsonfileid.append(the_dict['_id'])
        #print(spiderjsonfileid)
    for csid in csids:
        cskey = random.choice(cs_security_key)
        cs = ChemSpider(cskey)
        if csid in spiderjsonfileid:
            print('{0} has been in the file'.format(str(csid)))
            continue
        compound = cs.get_compound(csid)
        try:
            doc = {'_id': int(compound.csid), 'common_name': compound.common_name}
            sleep(random.uniform(0.2, 1.2))
            doc['molecular_weight'] = compound.molecular_weight
            sleep(random.uniform(0, 1.2))
            doc['molecular_formula'] = compound.molecular_formula
            doc['stdinchi'] = compound.stdinchi
            sleep(random.uniform(0.1, 0.5))
            doc['stdinchikey'] = compound.stdinchikey
            doc['smiles'] = compound.smiles
            sleep(random.uniform(1, 1.2))
            print("Thanks! ")
            with open('chemspiderdb.json', 'a') as jsonfile:
                json.dump(doc, jsonfile)
                jsonfile.write('\n')
        except Exception as e:
            print(str(e) + 'Invalid ID  is ' + str(compound.csid))
            with open('Invalid_ID.txt', 'a') as invalid_id:
                invalid_id.write(str(compound.csid) + '\n')
            continue
else:
    for csid in csids:
        cskey = random.choice(cs_security_key)
        cs = ChemSpider(cskey)
        compound = cs.get_compound(csid)
        try:
            doc = {'_id': int(compound.csid), 'common_name': compound.common_name}
            sleep(random.uniform(0.2, 1.2))
            doc['molecular_weight'] = compound.molecular_weight
            sleep(random.uniform(0, 1.2))
            doc['molecular_formula'] = compound.molecular_formula
            doc['stdinchi'] = compound.stdinchi
            sleep(random.uniform(0, 1.2))
            doc['stdinchikey'] = compound.stdinchikey
            doc['smiles'] = compound.smiles
            sleep(random.uniform(1, 1.2))
            print("Thanks! ")
            with open('chemspiderdb.json', 'a') as jsonfile:
                json.dump(doc, jsonfile)
                jsonfile.write('\n')
        except Exception as e:
            print(str(e) + 'Invalid ID  is ' + str(compound.csid))
            with open('Invalid_ID.txt', 'a') as invalid_id:
                invalid_id.write(str(compound.csid) + '\n')
            continue
print("Please email 'idrange.json', 'chemspiderdb.json' and 'Invalid_ID' to wangyt@neau.edu.cn")