from pytz import timezone
from datetime import datetime
import time as tm
import numpy as np
import socket, sys, json, random

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
mu, sigma = 25, 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

for i in range(SEND_NUM):

    time = datetime.now(timezone('Asia/Tokyo'))
    temperature = np.random.normal(mu, sigma, 1)

    json_body = {
        "measurement": measurement,
        "tags": {
            "host": HOST,
            "region": REGION
        },
        "time": str(time),
        "fields": {
            "value": int(temperature[0]),
        }
    }

    msg = json.dumps(json_body)
    msg += "\n"

    s.send(msg.encode('utf-8'))
    tm.sleep(SLP_TIME)
