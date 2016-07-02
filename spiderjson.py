import json
from chemspipy import ChemSpider
import random
from time import sleep
import os
import timeit

timerstart = timeit.default_timer()

if os.path.isfile('idrangeabc.json'):
    with open('idrangeabc.json', 'r') as idrangefile:
        idr = idrangefile.readline()
        idrange = json.loads(idr)
        csids = list(range(idrange['csidfrom'], idrange['csidto']))
        random.shuffle(csids)
        # print(csids)
else:
    print("You need a file named idrangeabc.json. Please contact me as soon as.")
    exit()


def tokenchoice():
    if os.path.isfile('Security_token.txt'):
        security_token = []
        with open('Security_token.txt', 'r') as security_token_file:
            for security_token_row in security_token_file.readlines():
                security_token.append(security_token_row.strip())
        return random.choice(security_token)
    else:
        print("You need Security_token.txt providing security token. Please contact me as soon as.")

if os.path.isfile('chemspiderdb.json'):
    spiderjsonfileid = []
    with open('chemspiderdb.json', 'r') as jsonfile:
        for f in jsonfile.readlines():
            the_dict = json.loads(f)
            spiderjsonfileid.append(the_dict['_id'])
            # print(spiderjsonfileid)
    for csid in csids:
        # cskey = random.choice(cs_security_key)
        cs = ChemSpider(tokenchoice())
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
            sleep(random.uniform(1, 5))
            with open('chemspiderdb.json', 'a') as jsonfile:
                json.dump(doc, jsonfile)
                jsonfile.write('\n')
            print("{0} Thanks! ".format(str(csid)))
        except Exception as e:
            print(str(e) + 'Invalid ID  is ' + str(compound.csid))
            with open('Invalid_ID.txt', 'a') as invalid_id:
                invalid_id.write(str(compound.csid) + '\n' + str(e) )
            continue
else:
    for csid in csids:
        # cskey = random.choice(cs_security_key)
        cs = ChemSpider(tokenchoice())
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
            with open('chemspiderdb.json', 'a') as jsonfile:
                json.dump(doc, jsonfile)
                jsonfile.write('\n')
            print("{0} Thanks! ".format(str(csid)))
        except Exception as e:
            print(str(e) + 'Invalid ID  is ' + str(compound.csid))
            with open('Invalid_ID.txt', 'a') as invalid_id:
                invalid_id.write(str(compound.csid) + '\n')
            continue
timerstop = timeit.default_timer()
print("Please email 'idrangeabc.json', 'chemspiderdb.json' and 'Invalid_ID' to wangyt@neau.edu.cn")
print("Your computer and you have worked for " + str((timerstop - timerstart) / 3600) + " hours!")
