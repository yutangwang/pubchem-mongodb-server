import json
import subprocess

jsonpath = 'D:\mongodb\\bin\compounds1.json'
mongoimport = "D:\mongodb\\bin\mongoimport"
print('Tidying JSON')
jsonfile = open(jsonpath, 'r')
data = json.load(jsonfile)
jsonfile.close()
jsonfile = open(jsonpath, 'w')
jsonfile.write('\n'.join([json.dumps(mol) for mol in data['PC_Compounds']]))
jsonfile.close()

print('Importing to MongoDB')
subprocess.call([mongoimport, '-d', 'pubchem', '-c', 'compoundpy', '--file', jsonpath])