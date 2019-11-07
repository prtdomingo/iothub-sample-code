# Azure IoT Hub Sample code using Python

### Initial Setup

* Run `pip install -r requirements.txt` on CLI 
* Add `CONNECTION_STRING` value in `.env` from your Azure IoT Hub - Devices Connection String
* Go to `shell.azure.com` and run `az extension add --name azure-cli-iot-ext` in the terminal to use IoT CLI commands
* To monitor the telemetry that Azure IoT Hub is getting, go to `shell.azure.com` and run the following in the terminal: `az iot hub monitor-events --hub-name {YourIoTHubName} --device-id {YourIoTDevice}`
