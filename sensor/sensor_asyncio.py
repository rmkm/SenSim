from pytz import timezone
from datetime import datetime
import time
import numpy as np
import socket, sys, json, random, yaml, signal
import asyncio


def signal_handler():
        print('You pressed Ctrl+C!')
        for task in asyncio.Task.all_tasks():
            task.cancel()


def reader(socket):
    data = socket.recv(100)
    print("Received:", data.decode())
    

async def sensor(loop, dictionary, delay):
    print("==> sensor start")

    await asyncio.sleep(delay)

    destinationIP = dictionary["destinationIP"]
    destinationPORT = dictionary["destinationPORT"]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(0)
    await loop.sock_connect(s, (destinationIP, destinationPORT))
    loop.add_reader(s, reader, s)

    measurement = dictionary["measurement"]
    host = dictionary["host"]
    region = dictionary["region"]
    numberOfData = dictionary["numberOfData"]
    sleepTime = dictionary["sleepTime"]

    for i in range(numberOfData):
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
        
        message = json.dumps(json_body)
        print('Send: %r' % message)
        s.send(message.encode())
        
        await asyncio.sleep(sleepTime)

    s.close()
    print("==> sensor end")


async def worker(loop):
    PATH = sys.argv[1]
    configFile = open(PATH, "r")
    configDict = yaml.load(configFile.read())
    numberOfSensor = configDict["numberOfSensor"];
    tasks = []
    for i in range(numberOfSensor):
        delay = random.randint(0,10)
        tasks.append(sensor(loop, configDict, delay))
    await asyncio.wait(tasks)


def main():
    if(len(sys.argv) != 2):
        print('Usage: ".py [path to yaml config file]"')
        sys.exit()
    event_loop = asyncio.get_event_loop()
    event_loop.add_signal_handler(signal.SIGINT, signal_handler)
    try:
        event_loop.run_until_complete(worker(event_loop))
    finally:
        event_loop.close()

if __name__ == '__main__':
    main()
