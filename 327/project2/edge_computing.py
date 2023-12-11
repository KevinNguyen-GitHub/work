import paho.mqtt.client as mqtt
import random
import json
import time
import numpy as np
import logging
import matplotlib.pyplot as plt

# Set up basic logging
logging.basicConfig(level=logging.INFO)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected with result code " + str(rc))
    else:
        logging.error("Failed to connect, return code %d", rc)


def on_message(client, userdata, msg):
    logging.info(f"Message received: {msg.topic} {msg.payload}")


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
    try:
        source_id = data['source_id']
        temperature = data['temperature']
        humidity = data['humidity']
        pressure = data['pressure']
        wind_speed = data['wind_speed']
        light_intensity = data['light_intensity']

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

    except KeyError as e:
        logging.error(f"Missing key in data: {e}")
    except Exception as e:
        logging.error(f"Error in processing data: {e}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect("mosquitto", 1883, 60)
    client.loop_start()
except Exception as e:
    logging.error(f"Unable to connect to MQTT broker: {e}")

try:
    while True:
        data = generate_data()
        process_data(data)
        client.publish("edge/data", json.dumps(data))
        time.sleep(1)
except KeyboardInterrupt:
    logging.info("Program interrupted, stopping MQTT client")
    client.loop_stop()
