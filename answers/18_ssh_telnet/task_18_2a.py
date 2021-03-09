# -*- coding: utf-8 -*-
"""
Task 18.2a


Copy the send_config_commands function from job 18.2 and add the log parameter.
The log parameter controls whether information is displayed about which device
the connection is to:
* if log is equal to True - information is printed
* if log is equal to False - information is not printed

By default, log is equal to True.

An example of how the function works:

In [13]: result = send_config_commands(r1, commands)
Connecting to 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, log=False)

In [15]:

The script should send command command to all devices from the devices.yaml file
using the send_config_commands function.
"""
from netmiko import ConnectHandler
import yaml


commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]


def send_config_commands(device, config_commands, log=True):
    if log:
        print(f"Connecting to {device['host']}...")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_config_commands(dev, commands))
