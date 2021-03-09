# -*- coding: utf-8 -*-
"""
Task 18.1b

Copy the send_show_command function from task 18.1a and rewrite it to handle
not only the exception that is raised when authentication fails on the device,
but also the exception that is raised when the IP address of the device
is not available.

When an error occurs, an exception message should be printed to standard output.

To check, change the IP address on the device or in the devices.yaml file.
"""
import yaml
import sys
from netmiko import ConnectHandler
from netmiko.ssh_exception import SSHException


def send_show_command(device, command):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
            return result
    except SSHException as error:
        print(error)


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]
    result = send_show_command(r1, command)
    print(result)
