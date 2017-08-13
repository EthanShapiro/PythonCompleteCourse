# DICTIONARIES IN PYTHON 3.6+ UP ARE ORDERED BY DEFAULT

d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'
d['f'] = 'F'

for k, v in d.items():
    print(k, v)

