# -*- coding: utf-8 -*-
"""
Task 21.4

Create function send_and_parse_show_command.

Function parameters:
* device_dict - a dict with connectin parameters for one device
* command - the command to be executed
* templates_path - path to the directory with TextFSM templates
* index - file index name, default value "index"

The function should connect to one device, send a show command using netmiko,
and then parse the command output using TextFSM.

The function should return a list of dictionaries with the results
of parsing the command output (as in task 21.1a):
* keys - names of variables in the TextFSM template
* values - parts of the output that correspond to variables

Check the operation of the function using the output
of the sh ip int br command and devices from devices.yaml.

"""
import os
from pprint import pprint
from netmiko import ConnectHandler
import yaml


def send_and_parse_show_command(device_dict, command, templates_path):
    if "NET_TEXTFSM" not in os.environ:
        os.environ["NET_TEXTFSM"] = templates_path
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command, use_textfsm=True)
    return output


if __name__ == "__main__":
    full_pth = os.path.join(os.getcwd(), "templates")
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        result = send_and_parse_show_command(
            dev, "sh ip int br", templates_path=full_pth
        )
        pprint(result, width=120)

# Second version without using use_textfsm in netmiko
from task_21_3 import parse_command_dynamic


def send_and_parse_show_command(device_dict, command, templates_path, index="index"):
    attributes = {"Command": command, "Vendor": device_dict["device_type"]}
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command)
        parsed_data = parse_command_dynamic(
            output, attributes, templ_path=templates_path, index_file=index
        )
    return parsed_data


if __name__ == "__main__":
    full_pth = os.path.join(os.getcwd(), "templates")
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        result = send_and_parse_show_command(
            dev, "sh ip int br", templates_path=full_pth
        )
        pprint(result, width=120)
