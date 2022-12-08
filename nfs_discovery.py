#!/usr/bin/env python3

import json

DISCOVERY_LIST = []
with open('/etc/fstab', 'rt') as f:
    data = f.readlines()
for line in data:
    if 'nfs' in line:
        # print(line.split()[1])
        DISCOVERY_LIST.append({"{#NFSNAME}": line.split()[1]})

JSON = json.dumps(DISCOVERY_LIST)
print(JSON)
