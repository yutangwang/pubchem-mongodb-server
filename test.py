import pubchempy as pcp

c= pcp.Compound.from_cid(5090)
print(c.inchi)