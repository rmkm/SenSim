from datetime import datetime
from collections import OrderedDict
import subprocess as sb
import sys
import json
import time, random

SEND_NUM = 10
SLP_TIME = 3
IP = "192.168.1.33"
PORT = 8080
dict = OrderedDict()

def netcat(ipaddr, port):
    cmd = 'nc %s %s' % (ipaddr, port)
    return sb.Popen(cmd.split(), stdin=sb.PIPE, encoding='utf8')

ncPipe = netcat(IP, PORT)

for i in range(SEND_NUM):

    device_id = "Test_Device_0001"
    date = datetime.now().replace(microsecond=0).isoformat()
    temperature = random.randint(0,100)
    dict["device_id"] = device_id
    dict["date"] = date
    dict["temperature"] = temperature

    msg = json.dumps(dict)
    msg += "\n"

    ncPipe.stdin.write(str(msg))
    ncPipe.stdin.flush()
    time.sleep(SLP_TIME)

#with open('normal.json', 'wt') as f:
#    json.dump(dict, f)

#print(dict)
