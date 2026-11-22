import time
import random
import json
import paho.mqtt.client as mqtt

machine_id = "MACHINE-001"

broker = "mqtt"
port = 1883

client = mqtt.Client()
client.connect(broker, port, 60)

client.loop_start()

while True:
    temperature = round(random.uniform(25, 45), 2)

    data = {
        "machine_id": machine_id,
        "temperature": temperature
    }

    message = json.dumps(data)

    client.publish(
        "factory/machine001/temperature",
        message
    )

    print("Sending Data:", message)
    time.sleep(3)
