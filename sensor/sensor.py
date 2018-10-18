from datetime import datetime
from collections import OrderedDict
from datetime import datetime
import subprocess as sb
import time as tm
import sys, json, random

if(len(sys.argv) != 4):
    print('Usage: ".py [ip_address] [port] [num of data to send]"')
    sys.exit()

SLP_TIME = 3
IP = sys.argv[1]
PORT = sys.argv[2]
SEND_NUM = sys.argv[3]

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

    msg = json.dumps(json_body)
    msg += "\n"

    ncPipe.stdin.write(str(msg))
    ncPipe.stdin.flush()
    tm.sleep(SLP_TIME)
