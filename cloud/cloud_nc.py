from influxdb import InfluxDBClient
from ast import literal_eval
import subprocess as sb
import sys

if(len(sys.argv) != 3):
    print('Usage: ".py [port] [DB name]" \n')
    sys.exit()

RECV_NUM = 100
TIME_OUT = 30
PORT = sys.argv[1]
DB = sys.argv[2]

def nclisten(port, time_out):
    cmd = "nc -l %s -w %s" % (port, time_out)
    return sb.Popen(cmd.split(), stdin=sb.PIPE, stdout=sb.PIPE, encoding='utf8')

client = InfluxDBClient(host='localhost', port=8086, database=DB)

ncPipe = nclisten(PORT, TIME_OUT)
dictList = []

for i in range(RECV_NUM):
    msg = ncPipe.stdout.readline()
    print(msg)
    dct = literal_eval(msg)
    dictList.append(dct)
    client.write_points(dictList)
