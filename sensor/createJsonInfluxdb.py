from datetime import datetime
import json

measurement = "temperature"
deviceID = "Test_Device_0001"
region = 1
time = datetime.now().replace(microsecond=0).isoformat()
temperature = 25

json_body = {
        "measurement": measurement,
        "tags": {
            "host": deviceID,
            "region": region
        },
        "time": time,
        "fields": {
            "value": temperature,
        }
    }

with open('test.json', 'wt') as f:
    json.dump(json_body, f)

print(json_body)
