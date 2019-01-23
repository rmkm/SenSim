"""Explanation of this script

==> This script contains sensor functions which can be called in 'sensor_asyncio.py'.
    Specify one of the functions below in a YAML file which is passed to
    'sensor_asyncio.py'.
==> Return value of given function is going to be sent.
==> Every function have to receive a list of argument. If you don't need it, just don't
    use it in your function.
==> Write your own sensor function you want!

"""

from pytz import timezone
from datetime import datetime
import random, json, string

"""temperature_sensor

Args:
    param1: (string) hostname of the sensor
    param2: (string) region where the sensor located
Return:
    JSON string

"""
def temperature(argList):
    assert len(argList) == 2, 'Length of argList must be 2'

    host = argList[0]
    host = 'host' + str(random.randint(10,99))
    region = argList[1]
    region = 'block' + str(random.randint(1,9))
    timeStamp = datetime.now(timezone('Asia/Tokyo')).strftime('%Y-%m-%d %H:%M:%S')
    temperature = random.randint(0,100)

    dictJson = {
        'measurement': 'temperature',
        'tags': {
            'host': host,
            'region': region
        },
        'time': str(timeStamp),
        'fields': {
            'value': temperature,
        }
    }

    return json.dumps(dictJson)


"""location_sensor

Args:
    Do not need
Return:
    JSON string

"""
def location(argList):
    latitude = random.randint(0, 25)
    longitude = random.choice(string.ascii_lowercase)
    timeStamp = datetime.now(timezone('Asia/Tokyo')).strftime('%Y-%m-%d %H:%M:%S')
    genderOption = 'MF'
    gender = random.choice(genderOption) 
    age = random.randint(20,70)

    dictJson = {
        'latitude': latitude,
        'longitude': longitude,
        'time': str(timeStamp),
        'gender': gender,
        'age': str(age)
    }

    return json.dumps(dictJson)


"""manufacturing_sensor

Args:
    Do not need
Return:
    JSON string

"""
def manufacturing(argsList):
    equipment_number = 'com1'
    timeStamp = datetime.now(timezone('Asia/Tokyo')).strftime('%Y-%m-%d %H:%M:%S')
    P1 = random.uniform(0,100)
    P2 = random.uniform(0,100)
    P3 = random.uniform(0,100)
    #P1 = random.uniform(0,20)
    #P2 = random.uniform(0,20)
    #P3 = random.uniform(0,20)

    dictJson = {
        'equipment_number': equipment_number,
        'time': str(timeStamp),
        'sensor_data': {
            'P1': round(P1, 2),
            'P2': round(P2, 2),
            'P3': round(P3, 2)
        }
        #},
        #'control_parameters': {
        #    'P1': round(P1, 2),
        #    'P2': round(P2, 2),
        #    'P3': round(P3, 2)
        #}
    }
    
    return json.dumps(dictJson)
