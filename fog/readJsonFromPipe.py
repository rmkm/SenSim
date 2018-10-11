import sys
import json
#from pprint import pprint
#from collections import OrderedDict
data = sys.stdin.read()
sys.stdin.close()

dict = json.loads(data)

for keys,values in dict.items():
    print key, "=>", val

with open('/home/morishima/workspace/simpleFog/fog/testlog.json', 'w') as f:
    f.write(json.dumps(dict))

criterion = 50

if dict["temperature"] >= criterion:
    msg = "forward"
    sys.stdout.write(str(msg))
    #sys.stdout.close()
else:
    msg = "drop"
    sys.stdout.write(str(msg))
    #sys.stdout.close()

sys.stdout.close()

#sys.stdout.write("test")
#sys.stdout.close()
