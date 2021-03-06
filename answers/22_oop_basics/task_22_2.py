# -*- coding: utf-8 -*-

"""
Task 22.2

Create a CiscoTelnet class that connects via Telnet to Cisco equipment.

When instantiating the class, a Telnet connection should be created,
as well as the transition to enable mode. The class must use the telnetlib
module to connect via Telnet.

The CiscoTelnet class, in addition to __init__, must have at least two methods:
* _write_line - takes a string as an argument and sends the string converted
  to bytes to the hardware and adds a line end character at the end.
  The _write_line method must be used inside the class.
* send_show_command - takes the show command as an argument and returns
  the output received from the device

__init__ method parameters:
* ip - IP address
* username - username
* password - password
* secret - enable password

An example of creating an instance of a class:
In [2]: from task_22_2 import CiscoTelnet

In [3]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}
   ...:

In [4]: r1 = CiscoTelnet(**r1_params)

In [5]: r1.send_show_command("sh ip int br")
Out[5]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                unassigned      YES manual up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nR1#'


Hint:
The _write_line method is needed in order to be able to shorten a line:
self.telnet.write(line.encode("ascii") + b"
")

to this:
self._write_line(line)

He shouldn't do anything else.
"""

import time
import telnetlib
import yaml


class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Username:")
        self._write_line(username)
        self.telnet.read_until(b"Password:")
        self._write_line(password)
        self._write_line("enable")
        self.telnet.read_until(b"Password:")
        self._write_line(secret)
        self._write_line("terminal length 0")
        time.sleep(1)
        self.telnet.read_very_eager()

    def _write_line(self, line):
        self.telnet.write(line.encode("ascii") + b"\n")

    def send_show_command(self, command):
        self._write_line(command)
        time.sleep(1)
        command_output = self.telnet.read_very_eager().decode("ascii")
        return command_output


if __name__ == "__main__":
    r1_params = {
        "ip": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    r1 = CiscoTelnet(**r1_params)
    print(r1.send_show_command("sh ip int br"))
