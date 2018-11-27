#from collections import OrderedDict
from pytz import timezone
from datetime import datetime
import time as tm
import socket, sys, json, random

#if(len(sys.argv) != 5):
#    print('Usage: ".py [path to json config file] [ip address] [port] [num of data to send]"')
#    sys.exit()
if(len(sys.argv) != 2):
    print('Usage: ".py [path to json config file]"')
    sys.exit()

PATH = sys.argv[1]
config_file = open(PATH, "r");
config_dict = json.loads(config_file.read())

HOST = config_dict["host"]
REGION = config_dict["region"]
PORT = config_dict["dst port"]
IP = config_dict["dst ip"]
SEND_NUM = config_dict["num"]
SLP_TIME = config_dict["sleep time"]

measurement = "temperature"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

for i in range(SEND_NUM):

    time = datetime.now(timezone('Asia/Tokyo'))
    temperature = random.randint(0,100)

    json_body = {
        "measurement": measurement,
        "tags": {
            "host": HOST,
            "region": REGION
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
