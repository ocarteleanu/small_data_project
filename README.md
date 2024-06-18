This project, called Sensortemp, integrates advanced technology to monitor and visualize temperature data in real-time. It combines hardware like the Raspberry Pi 3, Acurite 606 TX wireless temperature sensor, RTL-SDR dongle, Amazon smart plug, and a HP laptop with software tools such as Raspberry Pi OS, rtl_433, InfluxDB, and Grafana to create a robust monitoring system.

Hardware Overview:

Raspberry Pi 3 Kit: Acting as the central controller, it manages data collection and processing.
Acurite 606 TX Wireless Temperature Sensor: This sensor wirelessly transmits temperature data.
RTL-SDR Dongle with Antenna: Used to capture radio signals transmitted by the Acurite sensor.
Amazon Smart Plug: Enables remote power control for the Raspberry Pi setup.
HP Laptop: Used for development and initial setup of the system.

Software and Tools:

To bring this project to life, I utilized several software tools:

Raspberry Pi OS: The operating system for the Raspberry Pi 3, providing the foundation for all operations.
RTL-SDR USB Dongle Driver: Essential for interfacing with the RTL-SDR dongle to capture radio signals.
rtl_433: A powerful program that decodes radio transmissions from devices like our Acurite sensor.
InfluxDB: A robust time-series database where all temperature data is stored efficiently.
Grafana: An interactive web application used for visualizing and analyzing the data collected, providing real-time insights into temperature trends.
AWS EC2 Instance: Leveraged for scalability and reliability, hosting our application with a Tomcat server to serve Grafana dashboards.

Project Workflow:

Here’s how Sensortemp works:

Data Collection: The Acurite 606 TX sensor wirelessly transmits temperature data.
Signal Capture: The RTL-SDR dongle captures these radio signals.
Signal Decoding: Using rtl_433, the captured signals are decoded into readable temperature data. The rtl_433 program is installed on the Raspberry Pi where I created a service that runs automatically once the device is turned on:

/usr/local/bin/rtl_433  -C customary -F inhttp://34.194.24.230:8086/write?db=sensortemp -M time:unix:utc

In the line of code above, "customary" stands for Fahrenheit degrees, -F established the output format for the data processed, in this case is data written in an InfluxDB database located on the AWS EC2 instance and the timestamp uses the unix system.  

To turn on and off the Raspberry Pi remotely, I have used the Amazon smart plug and the Alexa app. 

Data Storage: The decoded data is then stored in InfluxDB, ensuring efficient management of time-series data.
Data Visualization:

Once stored, Grafana comes into play:

Real-time Monitoring: It retrieves data from InfluxDB and displays it on customizable dashboards.
Historical Analysis: Allows us to analyze temperature trends over time.



The integration with AWS EC2:

Hosting and Scalability: Enables us to host our application securely in the cloud, ensuring scalability to handle large volumes of data.
Tomcat Server: Used to serve Grafana, making our temperature data accessible from anywhere with an internet connection.

Programming languages used to fetch the data and create local GUI 	and a webpage on AWS EC2 :
- JavaScript
- Python
- HTML
- CSS
- InfluxQL
The full code is located in the corresponding files of this repository.
