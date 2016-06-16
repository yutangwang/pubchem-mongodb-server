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
    print(jsonpath)