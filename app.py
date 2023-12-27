import os
from influxdb import InfluxDBClient
import speedtest
import datetime

INFLUXDB_HOST = os.environ.get('INFLUXDB_HOST', 'localhost')
INFLUXDB_PORT = int(os.environ.get('INFLUXDB_PORT', 8086))
INFLUXDB_DB = os.environ.get('INFLUXDB_DB', 'your_database')

st = speedtest.Speedtest()
download_speed = st.download() / 1_000_000  # in Mbps
upload_speed = st.upload() / 1_000_000  # in Mbps
ping = st.results.ping  # in ms
jitter = st.results.jitter  # in ms
packet_loss = st.results.packet_loss  # in percentage

current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

data = [
    {
        "measurement": "internet_speed",
        "time": current_time,
        "fields": {
            "download_speed": download_speed,
            "upload_speed": upload_speed,
            "ping": ping,
            "jitter": jitter,
            "packet_loss": packet_loss
        }
    }
]

client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, database=INFLUXDB_DB)
client.write_points(data)
