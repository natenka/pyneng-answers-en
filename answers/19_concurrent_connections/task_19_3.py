# -*- coding: utf-8 -*-
"""
Task 19.3

Create a send_command_to_devices function that sends different show commands
to different devices in concurrent threads and then writes the output of the
commands to a file. The output from the devices in the file can be in any order.

Function parameters:
* devices - a list of dictionaries with parameters for connecting to devices
* commands_dict - a dictionary that specifies which device to send which command.
  Dictionary example - commands
* filename is the name of the file to which the output of all commands will be written
* limit - maximum number of concurrent threads (default 3)

The function returns None.

The output of the commands should be written to a plain text file in this
format (before the output of the command, you must write the hostname and
the command itself):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh int desc
Interface                      Status         Protocol Description
Et0/0                          up             up
Et0/1                          up             up
Et0/2                          admin down     down
Et0/3                          admin down     down
Lo9                            up             up
Lo19                           up             up
R3#sh run | s ^router ospf
router ospf 1
 network 0.0.0.0 255.255.255.255 area 0


You can create any additional functions to complete the task.

Check the operation of the function on devices from the devices.yaml file.
"""
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor, as_completed

from netmiko import ConnectHandler, NetMikoTimeoutException
import yaml


commands = {
    "192.168.100.1": "sh ip int br",
    "192.168.100.2": "sh arp",
    "192.168.100.3": "sh ip int br",
}


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        prompt = ssh.find_prompt()
    return f"{prompt}{command}\n{result}\n"


def send_command_to_devices(devices, commands_dict, filename, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [
            executor.submit(send_show_command, device, commands_dict[device["host"]])
            for device in devices
        ]
        with open(filename, "w") as f:
            for future in as_completed(futures):
                f.write(future.result())


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.load(f)
    send_command_to_devices(devices, commands, "result.txt")
