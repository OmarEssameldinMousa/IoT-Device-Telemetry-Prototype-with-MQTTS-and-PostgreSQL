import ssl
import json
import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.tls_set(
    ca_certs="cert.pem",
    certfile="cert.pem",
    keyfile="key.pem",
    tls_version=ssl.PROTOCOL_TLS
)

client.tls_insecure_set(True)  # 🔐 Disable hostname check (safe for local use only)

client.connect("localhost", 8883)

while True:
    data = {
        "device_id": "sensor-1",
        "temperature": 28.5,
        "humidity": 44,
        "timestamp": time.time()
    }
    client.publish("iot/devices", json.dumps(data))
    time.sleep(5)
