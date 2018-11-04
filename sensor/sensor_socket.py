#from collections import OrderedDict
from pytz import timezone
from datetime import datetime
#import subprocess as sb
import time as tm
import socket, sys, json, random

if(len(sys.argv) != 5):
    print('Usage: ".py [path to json config file] [ip address] [port] [num of data to send]"')
    sys.exit()

SLP_TIME = 3
PATH = sys.argv[1]
IP = sys.argv[2]
PORT = int(sys.argv[3])
SEND_NUM = int(sys.argv[4])

config_file = open(PATH, "r");
config_dict = json.loads(config_file.read())
measurement = "temperature"
host = config_dict["host"]
region = config_dict["region"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

for i in range(SEND_NUM):

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

    s.send(msg.encode('utf-8'))
    tm.sleep(SLP_TIME)
