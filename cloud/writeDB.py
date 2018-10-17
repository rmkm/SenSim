from influxdb import InfluxDBClient
from datetime import datetime                                                                                                                                                                
import json
import argparse 

measurement = "temperature"
deviceID = "Test_Device_0001"
region = 1
time = datetime.now().replace(microsecond=0).isoformat()
temperature = 25

json_body = [
    {
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
]

print(json_body)
print("\n")

client = InfluxDBClient(host='localhost', port=8086, database='example')

client.write_points(json_body)
