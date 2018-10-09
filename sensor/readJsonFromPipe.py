import sys
import json
#from pprint import pprint
#from collections import OrderedDict
data = sys.stdin.read()
sys.stdin.close()

dict = json.loads(data)

with open('/home/morishima/workspace/python/testlog.json', 'w') as f:
    f.write(json.dumps(dict))

sys.stdout.write("alright")
sys.stdout.close()
