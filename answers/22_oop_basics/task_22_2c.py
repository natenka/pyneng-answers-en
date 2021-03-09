# -*- coding: utf-8 -*-

"""
Task 22.2c

Copy the CiscoTelnet class from task 22.2b and modify the send_config_commands
method to check for errors.

The send_config_commands method must have an additional strict parameter:
* strict=True means that when an error is encountered, a ValueError must
  be raised (default)
* strict=False means that when an error is found, you only need to print
  the error message to the stdout

The method should return output similar to the send_config_set method of
netmiko (example output below). The text of the exception and error in
the example below.

An example of creating an instance of a class:
In [1]: from task_22_2c import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

In [4]: commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
In [5]: correct_commands = ['logging buffered 20010', 'ip http server']
In [6]: commands = commands_with_errors+correct_commands

Using the send_config_commands method:

In [7]: print(r1.send_config_commands(commands, strict=False))
When executing the command "logging 0255.255.1" on device 192.168.100.1, an error occurred -> Invalid input detected at '^' marker.
When executing the command "logging" on device 192.168.100.1, an error occurred -> Incomplete command.
When executing the command "a" on device 192.168.100.1, an error occurred -> Ambiguous command:  "a"
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"
R1(config)#logging buffered 20010
R1(config)#ip http server
R1(config)#end
R1#

In [8]: print(r1.send_config_commands(commands, strict=True))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-0abc1ed8602e> in <module>
----> 1 print(r1.send_config_commands(commands, strict=True))

...

ValueError: When executing the command "logging 0255.255.1" on device 192.168.100.1, an error occurred -> Invalid input detected at '^' marker.

"""
import time
import telnetlib
import yaml
from textfsm import clitable
import re


class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        self.ip = ip
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

    def _error_in_command(self, command, result, strict):
        regex = "% (?P<err>.+)"
        template = (
            'When executing the command "{cmd}" on device {device}, '
            'an error occurred -> {error}'
        )
        error_in_cmd = re.search(regex, result)
        if error_in_cmd:
            message = template.format(
                cmd=command, device=self.ip, error=error_in_cmd.group("err")
            )
            if strict:
                raise ValueError(message)
            else:
                print(message)

    def send_config_commands(self, commands, strict=True):
        output = ""
        if isinstance(commands, str):
            commands = [commands]
        self._write_line("conf t")
        for command in commands:
            self._write_line(command)
            time.sleep(1)
            result = self.telnet.read_very_eager().decode("ascii")
            output += result
            self._error_in_command(command, result, strict=strict)
        self._write_line("end")
        time.sleep(1)
        output += self.telnet.read_very_eager().decode("ascii")
        return output


if __name__ == "__main__":
    r1_params = {
        "ip": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    r1 = CiscoTelnet(**r1_params)
    print(r1.send_config_commands(commands, strict=False))
