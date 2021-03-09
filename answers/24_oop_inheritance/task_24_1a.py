# -*- coding: utf-8 -*-

"""
Task 24.1a

Copy and update the CiscoSSH class from task 24.1.

Before connecting via SSH, you need to check if the dictionary with the connection
parameters contains the following parameters: username, password, secret.
If any parameter is missing, ask the user for a value and then connect.
If all parameters are present, connect.

In [1]: from task_24_1a import CiscoSSH

In [2]: device_params = {
   ...:         'device_type': 'cisco_ios',
   ...:         'host': '192.168.100.1',
   ...: }

In [3]: r1 = CiscoSSH(**device_params)
Enter username: cisco
Enter password: cisco
Enter enable passwod: cisco

In [4]: r1.send_show_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

"""
from base_connect_class import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(self, **device_params):
        params = {
            "username": "Enter username: ",
            "password": "Enter password: ",
            "secret": "Enter enable password: ",
        }
        for param in params:
            if not param in device_params:
                device_params[param] = input(params[param])
        super().__init__(**device_params)
        self.ssh.enable()

