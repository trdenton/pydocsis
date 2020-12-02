# pydocsis
Control a Technicolor DPC3848V modem via python


Main script performs a reboot.  Docsis.py can do some SSID configuration tricks as well.

*Note: I no longer have this modem, so development will not proceed!*


## Requirements

 * python 'requests' module
 * A terrible DPC3848V modem


## Usage

```
usage: main.py [-h] [-u username] [-i ip address] password

positional arguments:
  password       Password for modem

optional arguments:
  -h, --help     show this help message and exit
  -u username    Admin username for modem [default cusadmin]
  -i ip address  IP address for modem [default 192.168.100.254]
```
