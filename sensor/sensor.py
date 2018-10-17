from datetime import datetime
from collections import OrderedDict
from datetime import datetime
import subprocess as sb
import sys, json, time, random

SEND_NUM = 10
SLP_TIME = 3
IP = sys.argv[1]
PORT = sys.argv[2]

if (IP is None) or (PORT is None):
    print('Usage: ".py [ip_address] [port]" \n')

def netcat(ipaddr, port):
    cmd = 'nc %s %s' % (ipaddr, port)
    return sb.Popen(cmd.split(), stdin=sb.PIPE, encoding='utf8')

ncPipe = netcat(IP, PORT)

measurement = "temperature"
deviceID = "MOKA-01"
region = 1

for i in range(SEND_NUM):

    time = datetime.now().replace(microsecond=0).isoformat()
    temperature = random.randint(0,100)

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

    msg = json.dumps(json_body)
    msg += "\n"

    ncPipe.stdin.write(str(msg))
    ncPipe.stdin.flush()
    time.sleep(SLP_TIME)
