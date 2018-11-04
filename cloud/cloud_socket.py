from influxdb import InfluxDBClient
from ast import literal_eval
#import subprocess as sb
import sys, socket

if(len(sys.argv) != 4):
    print('Usage: ".py [Host] [port] [DB name]" \n')
    sys.exit()

RECV_NUM = 100
TIME_OUT = 10
HOST = sys.argv[1]
PORT = int(sys.argv[2])
DB = sys.argv[3]

client = InfluxDBClient(host='localhost', port=8086, database=DB)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
conn.settimeout(TIME_OUT)

dictList = []

while 1:
    try:
        msg = conn.recv(256).decode('utf-8')
    except socket.timeout:
        break
    if not msg:
        break
    print(msg)
    dct = literal_eval(msg)
    dictList.append(dct)
    client.write_points(dictList)

conn.close()
