# Log Roomba Sensor Data to InfluxDB
import os
import time
import pytz
import datetime
from influxdb import InfluxDBClient
from pyroombaadapter import PyRoombaAdapter

# data = {'voltage', 'current', 'temperature', 'charge', 'capacity', 'oi-mode', 'charging-state'}

# set timezone
tz = pytz.timezone('EST')

# initialize the pyroomba adapter
def init_adapter():
    PORT = "/dev/ttyUSB0"
    adapter = PyRoombaAdapter(PORT)
    print(f"Setting mode to passive")
    adapter.change_mode_to_passive()
    print(f"Mode: {adapter.request_oi_mode()}")
    return adapter

# initialize the influxdb client
def init_client():
    host = os.environ.get('INFLUXDB_HOST')
    port = 8086
    user = os.environ.get('INFLUXDB_USER')
    password = os.environ.get('INFLUXDB_PASSWORD')
    database = os.environ.get('INFLUXDB_DATABASE')
    client = InfluxDBClient(host, port, user, password, database)
    return client

# read adapter sensors
def read_sensors(adapter):
    capacity = adapter.request_charge()
    charging_state = adapter.request_charging_state()
    charge = adapter.request_charge()
    current = adapter.request_current()
    oi_mode = adapter.request_oi_mode()
    temperature = adapter.request_temperature()
    voltage = adapter.request_voltage() / 1000
    data = {'capacity':capacity, 'charging-state':charging_state, 'charge':charge, 'current':current, 'oi-mode':oi_mode, 'temperature':temperature, 'voltage':voltage}
    return data

def populate_json():
    pass

adapter = init_adapter()
client = init_client()

while True:

    time.sleep(10) # Wait 60 seconds
    data = read_sensors(adapter)
    json_msg = [
    {
        "measurement": "sensor_reading",
        "tags": {
            "roombas": "levi"
        },
        "time": datetime.datetime.now(tz),
        "fields": {
            "capacity": data['capacity'],
            "charging-state": data['charging-state'],
            "charge": data['charge'],
            "current": data['current'],
            "oi-mode": data['oi-mode'],
            "temperature": data['temperature'],
            "volts": data['voltage']
        }
    }
]
    client.write_points(json_msg)
