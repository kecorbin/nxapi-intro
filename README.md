# NX-API Introduction

The purpose of this module is to introduce the NX-API capabilities of Cisco Nexus Switches.


## Prerequisites

Python 2 or Python 3
Requests

## Switch Configuration

To enable NX-API the following configuration must be completed on the Nexus switch

```
switch# conf t
Enter configuration commands, one per line. End with CNTL/Z.
switch(config)# feature nxapi
switch(config)# exit
switch# copy r s
[########################################] 100%
Copy complete.
switch#
```

## Getting Started

Start by modifying the credentials.py file and change the parameters to match your development environment

```
switch = '192.168.51.128'
user='admin'
password='changeme'
```

Test by executing nxapi_check_version.py


# More information

For more information you can visit Cisco DevNet

https://developer.cisco.com/site/nx-api/
