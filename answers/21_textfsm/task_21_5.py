# -*- coding: utf-8 -*-
"""
Task 21.5

Create function send_and_parse_command_parallel.

The send_and_parse_command_parallel function must run
the send_and_parse_show_command function from task 21.4 in concurrent threads.

Send_and_parse_command_parallel function parameters:
* devices - a list of dicts with connection parameters for devices
* command - command
* templates_path - path to the directory with TextFSM templates
* limit - maximum number of concurrent threads (default 3)

The function should return a dictionary:
* keys - the IP address of the device from which the output was received
* values - a list of dicts (the output returned by the send_and_parse_show_command function)

Dictionary example:
{'192.168.100.1': [{'address': '192.168.100.1',
                    'intf': 'Ethernet0/0',
                    'protocol': 'up',
                    'status': 'up'},
                   {'address': '192.168.200.1',
                    'intf': 'Ethernet0/1',
                    'protocol': 'up',
                    'status': 'up'}],
 '192.168.100.2': [{'address': '192.168.100.2',
                    'intf': 'Ethernet0/0',
                    'protocol': 'up',
                    'status': 'up'},
                   {'address': '10.100.23.2',
                    'intf': 'Ethernet0/1',
                    'protocol': 'up',
                    'status': 'up'}]}

Check the operation of the function using the output
of the sh ip int br command and devices from devices.yaml.
"""
from task_21_4 import send_and_parse_show_command
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
import os
import yaml


def send_and_parse_command_parallel(devices, command, templates_path, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result_all = [
            executor.submit(send_and_parse_show_command, device, command, templates_path)
            for device in devices
        ]
        output = {device["host"]: f.result() for device, f in zip(devices, result_all)}
    return output


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    command = "sh ip int br"
    path_dir = f"{os.getcwd()}/templates"
    pprint(send_and_parse_command_parallel(devices, command, path_dir))

