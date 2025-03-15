# influxdb_v2_python_client_write.py
import influxdb_client
import os
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = os.environ.get(INFLUXDB_BUCKET)
org = os.environ.get(INFLUXDB_ORG)
token = os.environ.get(INFLUXDB_TOKEN)
# Store the URL of your InfluxDB instance
url="https://" + INFLUXDB_HOST + ":8086"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
write_api.write(bucket=bucket, org=org, record=p)
