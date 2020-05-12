import pprint

stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)

pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)

tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
                                                           ('parrot', ('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(tup)

print(pprint.pformat(tup, depth=6))

# pprint.pp(tup) # 3.8

pprint.pprint(tup, depth=6)

print(pprint.isreadable(tup))
print(pprint.isrecursive(tup))

print("-----------------")

import json
import pprint
from urllib.request import urlopen

with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
    project_info = json.load(resp)['info']

pprint.pprint(project_info)

pprint.pprint(project_info, depth=1, width=60)
