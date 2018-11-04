from influxdb import InfluxDBClient
from ast import literal_eval
import sys, socket, select

if(len(sys.argv) != 4):
    print('Usage: ".py [Host] [port] [DB name]" \n')
    sys.exit()

RECV_NUM = 100
TIME_OUT = 10
HOST = sys.argv[1]
PORT = int(sys.argv[2])
DB = sys.argv[3]

client = InfluxDBClient(host='localhost', port=8086, database=DB)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind((HOST, PORT))
server.listen(5)
inputs = [server]
outputs = []

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
        else:
            msg = s.recv(256).decode('utf-8')
            if not msg:
                break
            print(msg)
            dct = literal_eval(msg)
            dictList = []
            dictList.append(dct)
            client.write_points(dictList)
    for s in exceptional:
        inputs.remove(s)
        s.close()
        del message_queues[s]

