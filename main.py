from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
import os
import json
from dotenv import load_dotenv
from sense_hat import SenseHat

# Load Environment Variable
load_dotenv()

# Go to .env file and add the connection string from IoT Hub - Devices you created
CONNECTION_STRING = os.environ.get('CONNECTION_STRING')

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def get_sense_data(sense):
    
    gyroscope_raw = sense.get_gyroscope_raw()
    compass_raw = sense.get_compass_raw()
    accelerometer_raw = sense.get_accelerometer_raw()
    
    data = ({
      "temperature": float("{0:.2f}".format(sense.get_temperature())),
      "humidity": float("{0:.2f}".format(sense.get_humidity())),
      "pressure": float("{0:.2f}".format(sense.get_pressure())),
      "gyroscopeX": float("{0:.2f}".format(gyroscope_raw["x"])),
      "gyroscopeY": float("{0:.2f}".format(gyroscope_raw["y"])),
      "gyroscopeZ": float("{0:.2f}".format(gyroscope_raw["z"])),
      "magnetometerX": float("{0:.2f}".format(compass_raw["x"])),
      "magnetometerY": float("{0:.2f}".format(compass_raw["y"])),
      "magnetometerZ": float("{0:.2f}".format(compass_raw["z"])),
      "accelerometerX": float("{0:.2f}".format(accelerometer_raw["x"])),
      "accelerometerY": float("{0:.2f}".format(accelerometer_raw["y"])),
      "accelerometerZ": float("{0:.2f}".format(accelerometer_raw["z"]))
    })
    
    return data

def send_telemetry():
    try:
        client = iothub_client_init()
        print ("IoT Hub device sending periodic messages, press Ctrl-C to exit")

        while True:        
            # Convert dictionary to string since send_message only accepts string, int, or float
            message = Message(str(get_sense_data(SenseHat())))
            print("Sending message: {}".format(message))
            client.send_message(message)

    except KeyboardInterrupt:
        print ("IoTHubClient sample stopped")


if __name__ == '__main__':
    print( "Press Ctrl-C to exit" )
    send_telemetry()
