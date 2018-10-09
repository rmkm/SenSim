import sys
import json
#from pprint import pprint
#from collections import OrderedDict

#dict = OrderedDict()

input_path = sys.argv[1]

with open(input_path, 'rt') as f:
    dict = json.load(f)

for k, v in dict.items():
    print(k, v)
print(dict["device_id"])
print(dict["date"])
print(dict["temperature"])
