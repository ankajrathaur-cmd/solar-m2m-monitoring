import paho.mqtt.client as mqtt
import json
import sqlite3

broker = "mqtt"
port = 1883

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to MQTT Broker!")
    client.subscribe("factory/+/temperature")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    conn = sqlite3.connect("database/machine_data.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO machine_data (machine_id, temperature) VALUES (?, ?)",
        (data["machine_id"], data["temperature"])
    )

    conn.commit()
    conn.close()

    print("Data Saved:", data)

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()
