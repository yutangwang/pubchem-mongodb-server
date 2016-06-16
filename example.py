ppp =  [
    {
        "value": {
            "ival": 1
        },
        "urn": {
            "label": "Compound",
            "release": "2011.04.04",
            "name": "Canonicalized",
            "datatype": 5
        }
    },
    {
        "value": {
            "fval": 219
        },
        "urn": {
            "software": "Cactvs",
            "version": "3.384",
            "datatype": 7,
            "label": "Compound Complexity",
            "release": "2011.09.13",
            "source": "xemistry.com",
            "implementation": "E_COMPLEXITY"
        }
    }
]
print(type(ppp[1]))
print(ppp[1])
print("-------urn--")
print(ppp[1]['urn'])

print(ppp[1]['urn']['datatype'])