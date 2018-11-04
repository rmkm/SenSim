from datetime import datetime
from collections import OrderedDict
from pytz import timezone
from datetime import datetime
import subprocess as sb
import time as tm
import sys, json, random

if(len(sys.argv) != 5):
    print('Usage: ".py [path to json config file] [ip_address] [port] [num of data to send]"')
    sys.exit()

SLP_TIME = 3
PATH = sys.argv[1]
IP = sys.argv[2]
PORT = sys.argv[3]
SEND_NUM = int(sys.argv[4])

def netcat(ipaddr, port):
    cmd = 'nc %s %s' % (ipaddr, port)
    return sb.Popen(cmd.split(), stdin=sb.PIPE, encoding='utf8')

config_file = open(PATH, "r");
config_dict = json.loads(config_file.read())

measurement = "temperature"
host = config_dict["host"]
region = config_dict["region"]

ncPipe = netcat(IP, PORT)

for i in range(SEND_NUM):

    #time = datetime.now().replace(microsecond=0).isoformat()
    time = datetime.now(timezone('Asia/Tokyo'))
    temperature = random.randint(0,100)

    json_body = {
        "measurement": measurement,
        "tags": {
            "host": host,
            "region": region
        },
        "time": str(time),
        "fields": {
            "value": temperature,
        }
    }

    msg = json.dumps(json_body)
    msg += "\n"

    ncPipe.stdin.write(str(msg))
    ncPipe.stdin.flush()
    tm.sleep(SLP_TIME)
