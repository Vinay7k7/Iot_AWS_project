#import random
#import boto3
#import ssl
#import paho.mqtt.client as mqtt
#
## AWS IoT credentials
#aws_endpoint = 'a2rf450pj1kjc-ats.iot.ap-south-1.amazonaws.com'  # Replace with your AWS IoT endpoint
#aws_topic = 'Topic01'  # Replace with your desired topic name
#
## Path to the device certificate and private key files
#certificate_path = '06094da32ffd6822d88bdf1689b446af03d3a935256309caf922e3af1d598c83-certificate.pem.crt'  # Replace with the path to your device certificate
#private_key_path = '06094da32ffd6822d88bdf1689b446af03d3a935256309caf922e3af1d598c83-private.pem.key'  # Replace with the path to your device private key
#root_ca_path = 'AmazonRootCA1.pem'  # Replace with the path to your root CA certificate
#
## Generate random values for water pressure, fire, and air pressure
#water_pressure = random.randint(1, 100)
#fire = random.randint(1, 100)
#air_pressure = random.randint(1, 100)
#
## Create an AWS IoT MQTT client
#mqtt_client = mqtt.Client(client_id='unique_client_id')
#
## Configure the TLS parameters
#mqtt_client.tls_set(root_ca_path, certfile=certificate_path, keyfile=private_key_path, cert_reqs=ssl.CERT_REQUIRED,
#                    tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
#
## Connect to AWS IoT
#mqtt_client.connect(aws_endpoint, port=8883)
#
## Prepare the payload
#payload = {
#    'water_pressure': water_pressure,
#    'fire': fire,
#    'air_pressure': air_pressure
#}
#
## Publish the payload to AWS IoT
#mqtt_client.publish(aws_topic, str(payload), qos=1)
#
## Disconnect from AWS IoT
#mqtt_client.disconnect()
#
#print("Values published successfully.")

















##import random
#import ssl
#import paho.mqtt.client as mqtt
#import json
### AWS IoT credentials
#aws_endpoint = 'a2rf450pj1kjc-ats.iot.ap-south-1.amazonaws.com'  # Replace with your AWS IoT endpoint
#aws_topic = 'Topic01'  # Replace with your desired topic name
#
## Path to the device certificate and private key files
#certificate_path = '06094da32ffd6822d88bdf1689b446af03d3a935256309caf922e3af1d598c83-certificate.pem.crt'  # Replace with the path to your device certificate
#private_key_path = '06094da32ffd6822d88bdf1689b446af03d3a935256309caf922e3af1d598c83-private.pem.key'  # Replace with the path to your device private key
#root_ca_path = 'AmazonRootCA1.pem'  # Replace with the path to your root CA certificate
#
#
## Generate random values for water pressure, fire, and air pressure
#water_pressure = random.randint(1, 100)
#fire = random.randint(1, 100)
#air_pressure = random.randint(1, 100)
#
## Create an AWS IoT MQTT client
#mqtt_client = mqtt.Client(client_id='unique_client_id')
#
## Configure the TLS parameters
#mqtt_client.tls_set(root_ca_path, certfile=certificate_path, keyfile=private_key_path, cert_reqs=ssl.CERT_REQUIRED,
#                    tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
#
## Define callback functions for MQTT events
#def on_connect(client, userdata, flags, rc):
#    if rc == 0:
#        print("Connected to AWS IoT")
#    else:
#        print("Failed to connect, error code:", rc)
#
#def on_publish(client, userdata, mid):
#    print("Published message ID:", mid)
#
#def on_disconnect(client, userdata, rc):
#    print("Disconnected from AWS IoT, result code:", rc)
#
#mqtt_client.on_connect = on_connect
#mqtt_client.on_publish = on_publish
#mqtt_client.on_disconnect = on_disconnect
#
## Connect to AWS IoT
#mqtt_client.connect(aws_endpoint, port=8883)
#mqtt_client.loop_start()  # Start the MQTT loop
#
## Prepare the payload
#payload = {
#    'water_pressure': water_pressure,
#    'fire': fire,
#    'air_pressure': air_pressure
#}
#
#payload1 = json.dumps(payload)
## Publish the payload to AWS IoT
#mqtt_client.publish(aws_topic, str(payload1), qos=1)
#
## Wait for the message to be published (adjust sleep duration if needed)
#mqtt_client.loop_stop()
#mqtt_client.disconnect()
#
#print("Values published successfully.")







import json
import random
import time
import ssl
import paho.mqtt.client as mqtt

# AWS IoT credentials
aws_endpoint = 'a2rf450pj1kjc-ats.iot.us-east-1.amazonaws.com'  # Replace with your AWS IoT endpoint
aws_topic = 'Safety_Monitoring/Topic01'  # Replace with your desired topic name

# Path to the device certificate and private key files
certificate_path = '44157f0b05857c268c7e32d4f5d606fc844bea57be53817893f6f9c56a195192-certificate.pem.crt'  # Replace with the path to your device certificate
private_key_path = '44157f0b05857c268c7e32d4f5d606fc844bea57be53817893f6f9c56a195192-private.pem.key'  # Replace with the path to your device private key
root_ca_path = 'AmazonRootCA1.pem'  # Replace with the path to your root CA certificate

# Create an AWS IoT MQTT client
mqtt_client = mqtt.Client(client_id='unique_client_id')

# Configure the TLS parameters
mqtt_client.tls_set(root_ca_path, certfile=certificate_path, keyfile=private_key_path, cert_reqs=ssl.CERT_REQUIRED,
                    tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

# Connect to AWS IoT
mqtt_client.connect(aws_endpoint, port=8883)
mqtt_client.loop_start()  # Start the MQTT loop

while True:
    Room_Names = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota"]
    # Static values for block and room
    
    block = "A-block"
    Thingid="Safety_Monitoring"
        
    # Generate random values for water pressure, fire, and air pressure

    room = random.choice(Room_Names)
    floor = random.randint(1, 11)

    water_pressure = random.randint(10, 100)
    fire = random.randint(273, 374)
    air_pressure = random.randint(1, 999)

    # Create a dictionary to hold the sensor data
    sensor_data = {
        
        'thingid':Thingid,
        'water_pressure': water_pressure,
        'fire': fire,
        'air_pressure': air_pressure,
        'block': block,
        'room': room,
        'floor':floor
        
    }


    print(json.dumps(sensor_data))

    # Convert the dictionary to a JSON string
    payload = json.dumps(sensor_data)

    # Publish the JSON payload to AWS IoT
    mqtt_client.publish(aws_topic, payload, qos=1)

    # Sleep for 80 seconds
    time.sleep(20)

mqtt_client.loop_stop()
mqtt_client.disconnect()
