/*
  Anders Grahn
  VT2024-DA642E-TS030: AI and Data Management for IoT-VT24
  Lab 2: Data Pre-processing and Visualization
  Task A2.1 Hey Nano! What's the Temp, Sub-exercises I
 
  Collect the temperature data from Arduino Nano RP2040 in Edge Impulse
  For the Edge Impulse data forwarder v1.23.1, I ran: edge-impulse-data-forwarder baud-rate 115200 --frequency 1

  Notes: To access the boards temperature data you need to install the LSM6DSOX library
*/

#include <Arduino_LSM6DSOX.h>

void setup() {
  Serial.begin(115200);

  // Start the built in IMU
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
}

void loop() {
  if (IMU.temperatureAvailable()) {
    int temperature_deg = 0;
    IMU.readTemperature(temperature_deg);

    Serial.println(temperature_deg);
    delay(1000);  // waits for a second to simulate 1Hz that we tell Edge Impulse to sample for
  }
}
