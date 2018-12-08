from influxdb import InfluxDBClient
from ast import literal_eval
import sys, socket, select, signal

if(len(sys.argv) != 4):
    print('Usage: ".py [Host] [port] [DB name]" \n')
    sys.exit()

def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        for i in range(len(inputs)):
            inputs[i].close()
        #print(inputs)
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

RECV_NUM = 100
TIME_OUT = 10
HOST = sys.argv[1]
PORT = int(sys.argv[2])
DB = sys.argv[3]

client = InfluxDBClient(host='localhost', port=8086, database=DB)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(0)
server.bind((HOST, PORT))
server.listen(20)
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
            msg = s.recv(1500).decode('utf-8')
            if not msg:
                break
            print(msg)
            print('\n')
            try:
                dct = literal_eval(msg)
            except SyntaxError:
                print("Invalid JSON data")
                continue
            dictList = []
            dictList.append(dct)
            client.write_points(dictList)
    for s in exceptional:
        inputs.remove(s)
        s.close()
        del message_queues[s]

