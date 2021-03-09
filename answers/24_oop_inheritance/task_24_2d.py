# -*- coding: utf-8 -*-

"""
Task 24.2d

Copy class MyNetmiko from task 24.2c or task 24.2b.

Add the ignore_errors parameter to the send_config_set method.
If ignore_errors=True, no error checking is needed and the method
should work exactly like the send_config_set method in netmiko.
If ignore_errors=False, errors should be checked.

By default, errors should be ignored.

In [2]: from task_24_2d import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [6]: r1.send_config_set('lo')
Out[6]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [7]: r1.send_config_set('lo', ignore_errors=True)
Out[7]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [8]: r1.send_config_set('lo', ignore_errors=False)
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-8-704f2e8d1886> in <module>()
----> 1 r1.send_config_set('lo', ignore_errors=False)

...
ErrorInCommand: When executing the command "lo" on device 192.168.100.1, an error occurred "Incomplete command."
"""
from netmiko.cisco.cisco_ios import CiscoIosSSH
import re
from task_24_2a import ErrorInCommand


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()

    def _check_error_in_command(self, command, result):
        regex = "^.+\n(.*\n)*% (?P<err>.+)"
        message = (
            'The "{}" command was executed with the error "{}" on the device {}'
        )
        error_in_cmd = re.search(regex, result)
        if error_in_cmd:
            raise ErrorInCommand(
                message.format(
                    cmd=command, device=self.host, error=error_in_cmd.group("err")
                )
            )

    def send_command(self, command, *args, **kwargs):
        command_output = super().send_command(command, *args, **kwargs)
        self._check_error_in_command(command, command_output)
        return command_output

    def send_config_set(self, commands, ignore_errors=True, *args, **kwargs):
        if ignore_errors:
            output = super().send_config_set(commands, *args, **kwargs)
            return output
        if isinstance(commands, str):
            commands = [commands]
        commands_output = ""
        commands_output += self.config_mode()
        for command in commands:
            result = super().send_config_set(command, exit_config_mode=False)
            commands_output += result
            self._check_error_in_command(command, result)
        commands_output += self.exit_config_mode()
        return commands_output
