import paho.mqtt.client as mqtt
import json
import time
import numpy as np
import ssl
import matplotlib.pyplot as plt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("edge/data")


def on_message(client, userdata, msg):
    start_time = time.time()
    data = json.loads(msg.payload)
    process_data(data)
    end_time = time.time()
    processing_latency = end_time - start_time
    print(f"Centralized Processing Latency: {processing_latency} seconds")


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

    # Visualize data (line chart for humidity)
    # plt.figure(figsize=(8, 4))
    # plt.plot(humidity)
    # plt.title(f'Humidity Data (Source {source_id})')
    # plt.xlabel('Time')
    # plt.ylabel('Humidity (%)')
    # plt.grid(True)
    # plt.show()

    # You can similarly visualize other data attributes or perform more analysis as needed.


client = mqtt.Client()
client.tls_set(ca_certs="/ssl/ca.crt",
               certfile="/ssl/client.crt",
               keyfile="/ssl/client.key",
               tls_version=ssl.PROTOCOL_TLSv1_2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("mosquitto", 8883, 60)  # TLS port
client.loop_forever()
