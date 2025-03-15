from influxdb import InfluxDBClient
import os

json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2024-11-10T23:00:00Z",
        "fields": {
            "value": 0.64
        }
    }
]
host = os.environ['INFLUXDB_HOST']
port = 8086
user = os.environ['INFLUXDB_USER']
password = os.environ['INFLUXDB_PASSWORD']
database = os.environ['INFLUXDB_DATABASE']
client = InfluxDBClient(host, port, user, password, database)
# client.create_database('example')
client.write_points(json_body)
result = client.query('select value from cpu_load_short;')
print("Result: {0}".format(result))
