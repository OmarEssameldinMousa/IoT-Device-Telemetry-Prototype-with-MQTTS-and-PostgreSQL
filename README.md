
# 🔐 IoT Device Telemetry Prototype with MQTTS and PostgreSQL

This is a simple, production-style prototype that demonstrates how to securely transmit real-time IoT device data using **MQTTS (MQTT over TLS)** and store it in a **PostgreSQL** database.

---

## 🚀 Features

- Secure **MQTTS** communication using self-signed TLS certificates
- Simulated IoT **publisher** sending JSON data (temperature, humidity)
- **Subscriber** listens to a topic and writes data into a structured PostgreSQL table
- Fully local, testable setup — great starting point for scalable IoT architectures

---

## 🧩 Tech Stack

| Component     | Description                                   |
|---------------|-----------------------------------------------|
| Python        | MQTT publisher/subscriber + PostgreSQL client |
| Paho-MQTT     | MQTT client library for Python                |
| Mosquitto     | MQTT broker with TLS (port `8883`)            |
| PostgreSQL    | Database to store device telemetry            |
| OpenSSL       | For generating self-signed certificates       |

---

## 📁 Folder Structure

```

iot-mqtts-prototype/
├── cert.pem                # Self-signed certificate
├── key.pem                 # Private key for TLS
├── mosquitto.conf          # Mosquitto config with TLS enabled
├── publisher.py            # Simulated IoT device publishing telemetry
├── subscriber.py           # MQTT subscriber writing to PostgreSQL
├── README.md               # Project documentation

````

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

Make sure you have Python 3.8+, PostgreSQL, and Mosquitto installed.

Install Python packages:
```bash
pip install paho-mqtt psycopg2-binary
````

### 2. Generate TLS Certificate (optional if already included)

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
```

### 3. Configure and Run Mosquitto

Create `mosquitto.conf`:

```conf
listener 8883
certfile cert.pem
keyfile key.pem
cafile cert.pem
allow_anonymous true
```

Start the broker:

```bash
mosquitto -c mosquitto.conf
```

### 4. Setup PostgreSQL

Run:

```bash
sudo -u postgres psql
```

Then:

```sql
CREATE DATABASE iot;
CREATE USER omar WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE iot TO omar;
\q
```

> Ensure your PostgreSQL server is running and listening on `localhost:5432`.

---

## 🚦 Run the System

### Start the Subscriber (consumer):

```bash
python3 subscriber.py
```

### Start the Publisher (producer):

```bash
python3 publisher.py
```

You should see:

```
✅ Data saved: {'device_id': 'sensor-1', 'temperature': 28.5, ...}
```
# IoT-Device-Telemetry-Prototype-with-MQTTS-and-PostgreSQL
