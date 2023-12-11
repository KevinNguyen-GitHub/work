import paho.mqtt.client as mqtt
import random
import json
import time
import numpy as np
import logging
import matplotlib.pyplot as plt

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# shows that the docker is connected
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected with result code " + str(rc))
    else:
        logging.error("Failed to connect, return code %d", rc)


def on_message(client, userdata, msg):
    logging.info(f"Message received: {msg.topic} {msg.payload}")

# create the data to be processed
def generate_data(num_readings=1000):
    temperature_readings = np.random.uniform(25.0, 30.0, num_readings).tolist()
    humidity_readings = np.random.uniform(45.0, 55.0, num_readings).tolist()
    pressure_readings = np.random.uniform(950.0, 1050.0, num_readings).tolist()
    wind_speed_readings = np.random.uniform(0.0, 20.0, num_readings).tolist()
    light_intensity_readings = np.random.uniform(0.0, 1000.0, num_readings).tolist()

    complex_data = [
        {'timestamp': i, 'value': np.random.random()}
        for i in range(num_readings)
    ]

    return {
        'source_id': 1,
        'temperature': temperature_readings,
        'humidity': humidity_readings,
        'pressure': pressure_readings,
        'wind_speed': wind_speed_readings,
        'light_intensity': light_intensity_readings,
        'additional_data': complex_data
    }

# process the data
def process_data(data):
    start_time = time.time()
    try:
        source_id = data['source_id']
        temperature = data['temperature']
        humidity = data['humidity']
        pressure = data['pressure']
        wind_speed = data['wind_speed']
        light_intensity = data['light_intensity']
        complex_data = data['additional_data']

    except KeyError as e:
        logging.error(f"Missing key in data: {e}")
    except Exception as e:
        logging.error(f"Error in processing data: {e}")
    finally:
        end_time = time.time()
        processing_time = end_time - start_time
        logging.info(f"Edge Processing Time: {processing_time} seconds")

# connects to mqtt
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# client.tls_set(ca_certs="/ssl/ca.crt",
#                certfile="/ssl/client.crt",
#                keyfile="/ssl/client.key",
#                tls_version=ssl.PROTOCOL_TLSv1_2)

# client.connect("mosquitto", 8883, 60)  # TLS port

# connect to msqtt broker
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
    client.loop_stop() # end the program
