import paho.mqtt.client as mqtt
import random
import json
import time
import numpy as np
import ssl
import matplotlib.pyplot as plt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def generate_data():
    return {
        'source_id': 1,
        'temperature': np.random.uniform(25.0, 30.0),
        'humidity': np.random.uniform(45.0, 55.0),
        'pressure': np.random.uniform(950.0, 1050.0),
        'wind_speed': np.random.uniform(0.0, 20.0),
        'light_intensity': np.random.uniform(0.0, 1000.0)
    }


def process_data(data):
    source_id = data['source_id']
    temperature = data['temperature']
    humidity = data['humidity']
    pressure = data['pressure']
    wind_speed = data['wind_speed']
    light_intensity = data['light_intensity']

    # Calculate statistical features
    temperature_mean = np.mean(temperature)
    humidity_mean = np.mean(humidity)

    # Visualize data (line chart for temperature)
    # plt.figure(figsize=(8, 4))
    # plt.plot(temperature)
    # plt.title(f'Temperature Data (Source {source_id})')
    # plt.xlabel('Time')
    # plt.ylabel('Temperature (°C)')
    # plt.grid(True)
    # plt.show()

    # You can similarly visualize other data attributes or perform more analysis as needed.


client = mqtt.Client()
client.tls_set(ca_certs="ca.crt", certfile="client.crt", keyfile="client.key",
               tls_version=ssl.PROTOCOL_TLSv1_2)
client.on_connect = on_connect
client.connect("mqtt_broker_address", 8883, 60)  # TLS port

client.loop_start()

while True:
    data = generate_data()
    process_data(data)
    client.publish("edge/data", json.dumps(data))
    time.sleep(1)

client.loop_stop()
