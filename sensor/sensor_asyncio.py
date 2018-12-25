from pytz import timezone
from datetime import datetime
import numpy as np
import time, socket, sys, json, random, yaml, signal, asyncio
import generator

def signal_handler():
        print('You pressed Ctrl+C!')
        for task in asyncio.Task.all_tasks():
            task.cancel()


def reader(socket, start_time):
    end_time = time.clock_gettime(time.CLOCK_MONOTONIC)
    print("RTT:", end_time - start_time)
    data = socket.recv(100)
    print("Received:", data.decode())
    

async def sensor(loop, confDict, delay):
    print("==> sensor start")

    await asyncio.sleep(delay)

    destinationIP = confDict["destinationIP"]
    destinationPORT = confDict["destinationPORT"]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(0)
    await loop.sock_connect(s, (destinationIP, destinationPORT))

    function = confDict["function"]
    args = confDict["args"]
    numberOfData = confDict["numberOfData"]
    sleepTime = confDict["sleepTime"]

    for i in range(numberOfData):
        data = getattr(generator, function)(args)
        
        print('Send: %r' % data)
        start = time.clock_gettime(time.CLOCK_MONOTONIC)
        s.send(data.encode())
        loop.add_reader(s, reader, s, start)
        
        await asyncio.sleep(sleepTime)

    s.close()
    print("==> sensor end")


async def worker(loop, confDict):
    numberOfSensor = confDict["numberOfSensor"]
    tasks = []
    if numberOfSensor == 1:
        tasks.append(sensor(loop, confDict, 0))
    else:
        for i in range(numberOfSensor):
            delay = random.uniform(0,10)
            tasks.append(sensor(loop, confDict, delay))
    await asyncio.wait(tasks)


def main():
    assert len(sys.argv) == 2, 'Usage: "[this_script.py] [config.yaml]"'
    PATH = sys.argv[1]
    confFile = open(PATH, "r")
    confD = yaml.load(confFile.read())
    event_loop = asyncio.get_event_loop()
    event_loop.add_signal_handler(signal.SIGINT, signal_handler)
    try:
        event_loop.run_until_complete(worker(event_loop, confD))
    finally:
        event_loop.close()

if __name__ == '__main__':
    main()
