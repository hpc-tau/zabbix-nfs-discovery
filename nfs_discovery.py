#!/usr/bin/env python3

import json

DISCOVERY_LIST = []
with open('fstab', 'rt') as f:
    data = f.readlines()
for line in data:
    if 'nfs' in line and not line.startswith('#'):
    # if 'nfs' in line:
        # print(line.split()[1])
        DISCOVERY_LIST.append({"{#NFSNAME}": line.split()[1]})

JSON = json.dumps(DISCOVERY_LIST)
# print(JSON)

for i in json.loads(JSON):
    print(i)
print(len(DISCOVERY_LIST))
