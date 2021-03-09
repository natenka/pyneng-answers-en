# -*- coding: utf-8 -*-

"""
Task 24.1

Create a CiscoSSH class that inherits the BaseSSH class
from the base_connect_class.py file.

Create an __init__ method in the CiscoSSH class so that after connecting
via SSH, it switches to enable mode.

To do this, the __init__ method must first call the __init__ method of
the BaseSSH class, and then switch to enable mode.

In [2]: from task_24_1 import CiscoSSH

In [3]: r1 = CiscoSSH(**device_params)


In [4]: r1.send_show_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

"""
from base_connect_class import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.ssh.enable()
