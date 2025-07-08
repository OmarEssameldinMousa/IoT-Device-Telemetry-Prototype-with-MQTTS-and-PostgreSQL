import ssl
import json
import paho.mqtt.client as mqtt
import psycopg2

# PostgreSQL connection
conn = psycopg2.connect(
    database="iot",
    user="omar",
    password="password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS device_data (
        device_id TEXT,
        temperature FLOAT,
        humidity FLOAT,
        timestamp DOUBLE PRECISION
    );
""")
conn.commit()

# MQTT message handler
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        cur.execute(
            "INSERT INTO device_data (device_id, temperature, humidity, timestamp) VALUES (%s, %s, %s, %s)",
            (
                payload['device_id'],
                payload['temperature'],
                payload['humidity'],
                payload['timestamp']
            )
        )
        conn.commit()
        print("✅ Data saved:", payload)
    except Exception as e:
        print("❌ Error handling message:", e)

# Initialize MQTT client
client = mqtt.Client()
client.tls_set(
    ca_certs="cert.pem",
    certfile="cert.pem",
    keyfile="key.pem",
    tls_version=ssl.PROTOCOL_TLS
)
client.tls_insecure_set(True)  # Disable hostname verification for self-signed certs

# Connect and subscribe
client.connect("localhost", 8883)
client.subscribe("iot/devices")
client.on_message = on_message
client.loop_forever()
