# RaspberryPiMQTT

Installed Raspberry Pi OS Lite to the Raspberry Pi. 
Enabled WiFi and SSH using raspi-config. 
Installed mosquitto MQTT broker and tested to ensure it is working locally. 
Tested localhost with mosquitto MQTT broker to ensure localhost is receiving the MQTT messages it sends.
Can receive JSON mqtt messages.

TODO NEXT:
test TLS/SSL on MQTT transmission to ensure security

## Notes on installing pyodbc on Debian 12 (Raspbian OS Lite):
Follow this link for instructions* but there is a small change:
https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017&tabs=debian18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline

*Run the following command before running the command under Debian 12 on the instructions because apt-key is deprecated. 

```curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | sudo tee /usr/share/keyrings/microsoft-prod.gpg > /dev/null```
