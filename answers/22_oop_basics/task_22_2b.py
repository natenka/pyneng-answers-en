# -*- coding: utf-8 -*-

"""
Task 22.2b

Copy the CiscoTelnet class from task 22.2a and add the send_config_commands method.

The send_config_commands method must be able to send one configuration mode
command and a list of commands. The method should return output similar
to the send_config_set method of netmiko (example output below).


An example of creating an instance of a class:
In [1]: from task_22_2b import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

Using the send_config_commands method:

In [5]: r1.send_config_commands('logging 10.1.1.1')
Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 10.1.1.1\r\nR1(config)#end\r\nR1#'

In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
Out[6]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop55\r\nR1(config-if)#ip address 5.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'

"""
import time
import telnetlib
import yaml
from textfsm import clitable


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

    def send_show_command(self, command, parse=True, templates="templates"):
        self._write_line(command)
        time.sleep(1)
        command_output = self.telnet.read_very_eager().decode("ascii")
        if not parse:
            return command_output
        attributes = {"Command": command, "Vendor": "cisco_ios"}
        cli = clitable.CliTable("index", templates)
        cli.ParseCmd(command_output, attributes)
        return [dict(zip(cli.header, row)) for row in cli]

    def send_config_commands(self, commands):
        if isinstance(commands, str):
            commands = [commands]
        commands = ["conf t", *commands, "end"]
        for command in commands:
            self._write_line(command)
            time.sleep(1)
        return self.telnet.read_very_eager().decode("ascii")


if __name__ == "__main__":
    r1_params = {
        "ip": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    r1 = CiscoTelnet(**r1_params)
    print(r1.send_config_commands("logging 10.1.1.1"))
    print(
        r1.send_config_commands(
            ["interface loop55", "ip address 5.5.5.5 255.255.255.255"]
        )
    )
