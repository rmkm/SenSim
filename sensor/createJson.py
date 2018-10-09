from datetime import datetime
from collections import OrderedDict
import json

dict = OrderedDict()

device_id = "Test_Device_0001"
date = datetime.now().replace(microsecond=0).isoformat()
temperature = 25

dict["device_id"] = device_id
dict["date"] = date
dict["temperature"] = temperature

with open('normal.json', 'wt') as f:
    json.dump(dict, f)

print(dict)
