"""
    Read Roomba sensors
"""
from time import sleep
from pyroombaadapter import PyRoombaAdapter

PORT = "/dev/ttyUSB0"
adapter = PyRoombaAdapter(PORT)
adapter.change_mode_to_passive()
print(f"Mode: {adapter.request_oi_mode()}")

# Request sensor value manually
#print(f"Charging_state: {adapter.request_charging_state()}")
#print(f"Voltage: {adapter.request_voltage()}")
#print(f"Current: {adapter.request_current()}")
#print(f"Temperature: {adapter.request_temperature()}")
#print(f"Charge: {adapter.request_charge()}")
#print(f"Capacity: {adapter.request_capacity()}")
#print(f"OI Mode: {adapter.request_oi_mode()}")
# print(f"Distance: {adapter.request_distance()}")
# print(f"Angle: {adapter.request_angle()}")
