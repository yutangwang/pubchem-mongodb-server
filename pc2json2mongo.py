import glob
import os
import gzip
import subprocess
import json

compounddir = '/g5/home/yw518/asn/ftp.ncbi.nlm.nih.gov/pubchem/Compound/CURRENT-Full/ASN'
asnspec = '/g5/home/yw518/datatool/bin/pubchem.asn'
datatool = '/g5/home/yw518/datatool/bin/datatool'
mongoimport = 'mongoimport'

for gzpath in glob.glob(os.path.join(compounddir, 'Compound_*.asn.gz')):
    asnpath = gzpath[:-3]
    jsonpath = gzpath[:-7] + '.json'
    print('Un-gzipping')
    gz = gzip.open(gzpath, 'rb')
    asn = gz.read()
    gz.close()
    with open(asnpath, 'wb') as asnfile:
        asnfile.write(asn)

    print('Converting to JSON')
    subprocess.call([datatool, '-m', asnspec, '-d', asnpath, '-pj', jsonpath, '-t', 'PC-Compounds'])

    print('Tidying JSON')
    jsonfile = open(jsonpath, 'r')
    data = json.load(jsonfile)
    jsonfile.close()
    jsonfile = open(jsonpath, 'w')
    jsonfile.write('\n'.join([json.dumps(mol) for mol in data['PC_Compounds']]))
    jsonfile.close()

    print('Importing to MongoDB')
    subprocess.call([mongoimport, '--host', 'ciipro.rutgers.edu', '--port', '27017', '-d', 'master', '-c', 'pcompounds', '-u', 'yw518', '-p', 'tmp2016', '--authenticationDatabase', 'admin', jsonpath])
#  mongoimport '--host', 'ciipro.rutgers.edu', '--port', '27017', '-d', 'learnDB', '-c' 'pcompounds', '-u', 'yw518', '-p', 'tmp2016', '--authenticationDatabase', 'admin',  --file compounds1.json