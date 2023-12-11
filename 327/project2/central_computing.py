import json
import logging
import time

import numpy as np
import paho.mqtt.client as mqtt

# Set up logging
logging.basicConfig(level=logging.INFO)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected with result code " + str(rc))
        client.subscribe("edge/data")
    else:
        logging.error("Failed to connect, return code %d", rc)


def on_message(client, userdata, msg):
    try:
        start_time = time.time()
        data = json.loads(msg.payload)
        process_data(data)
        end_time = time.time()
        processing_latency = end_time - start_time
        logging.info(f"Centralized Processing Latency: {processing_latency} seconds")
    except json.JSONDecodeError:
        logging.error("Unable to decode JSON message")
    except Exception as e:
        logging.error(f"Error processing message: {e}")


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

        # Visualize data (line chart for humidity)
        # plt.figure(figsize=(8, 4))
        # plt.plot(humidity)
        # plt.title(f'Humidity Data (Source {source_id})')
        # plt.xlabel('Time')
        # plt.ylabel('Humidity (%)')
        # plt.grid(True)
        # plt.show()

    except KeyError as e:
        logging.error(f"Missing key in data: {e}")
    except Exception as e:
        logging.error(f"Error in processing data: {e}")



client = mqtt.Client()
# client.tls_set(ca_certs="/ssl/ca.crt",
#                certfile="/ssl/client.crt",
#                keyfile="/ssl/client.key",
#                tls_version=ssl.PROTOCOL_TLSv1_2)
client.on_connect = on_connect
client.on_message = on_message

# client.connect("mosquitto", 8883, 60)  # TLS port
client.connect("mosquitto", 1883, 60)  # TLS port
client.loop_forever()


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
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect("mosquitto", 1883, 60)
    client.loop_start()
except Exception as e:
    logging.error(f"Unable to connect to MQTT broker: {e}")

try:
    while True:
        time.sleep(1)  # Keep the main thread alive.
except KeyboardInterrupt:
    logging.info("Stopping MQTT client")
    client.loop_stop()
