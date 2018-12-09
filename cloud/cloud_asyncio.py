from influxdb import InfluxDBClient 
from ast import literal_eval
import socket, sys, json, random, yaml, signal
import asyncio

if(len(sys.argv) != 2):
    print('Usage: ".py [path to json config file]"')
    sys.exit()

PATH = sys.argv[1]
configFile = open(PATH, "r")
configDict = yaml.load(configFile.read())

host = configDict["host"]
port = configDict["port"]
if "database" in configDict:
    DBname = configDict["database"]
    client = InfluxDBClient(host='localhost', port=8086, database=DBname)

def signal_handler():
        print('You pressed Ctrl+C!')
        for task in asyncio.Task.all_tasks():
            task.cancel()


async def listener(loop, connection, address):
    while True:
        msg = await loop.sock_recv(connection, 1500)
        if not msg:
            break
        msg = msg.decode('utf-8')
        try:
            dct = literal_eval(msg)
        except SyntaxError:
            print("Invalid JSON data")
            continue
        print("From {}: {}".format(address, msg))
        dictList = []
        dictList.append(dct)
        try:
            client.write_points(dictList)
        except NameError:
            continue
    connection.close()


async def worker(loop, sock):
    while True:
        conn, addr = await loop.sock_accept(sock)
        print("New connection {}".format(addr))
        loop.create_task(listener(loop, conn, addr))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(False)
    sock.bind((host, port))
    sock.listen()

    event_loop = asyncio.get_event_loop()
    event_loop.add_signal_handler(signal.SIGINT, signal_handler)
    try:
        event_loop.run_until_complete(worker(event_loop, sock))
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()
