import time
import random
import json
import paho.mqtt.client as mqtt

machine_id = "MACHINE-002"

broker = "localhost"
port = 1883

client = mqtt.Client()
client.connect(broker, port, 60)
client.loop_start()

while True:
    temperature = round(random.uniform(30, 50), 2)

    data = {
        "machine_id": machine_id,
        "temperature": temperature
    }

    message = json.dumps(data)

    client.publish(
        "factory/machine002/temperature",
        message
    )

    print("Sending Data:", message)

    time.sleep(3)
