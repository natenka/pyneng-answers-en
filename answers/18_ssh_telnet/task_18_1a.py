# -*- coding: utf-8 -*-
"""
Task 18.1a

Copy the send_show_command function from task 18.1 and rewrite it to handle
the exception that is thrown on authentication failure on the device.

When an error occurs, an exception message should be printed to stdout.

To verify, change the password on the device or in the devices.yaml file.

"""
import yaml
import sys
from netmiko import ConnectHandler
from paramiko.ssh_exception import AuthenticationException


def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            return result
    except AuthenticationException as error:
        print(error)


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        result = send_show_command(dev, command)
        print(result)
