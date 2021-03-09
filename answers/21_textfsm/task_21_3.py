# -*- coding: utf-8 -*-
"""
Task 21.3

Create function parse_command_dynamic.

Function parameters:
* command_output - command output (string)
* attributes_dict - an attribute dict containing the following key-value pairs:
 * 'Command': command
 * 'Vendor': vendor
* index_file is the name of the file where the correspondence between commands
  and templates is stored. The default is "index"
* templ_path - directory where templates are stored. The default is "templates"

The function should return a list of dicts with the results
of parsing the command output (as in task 21.1a):
* keys - names of variables in the TextFSM template
* values - parts of the output that correspond to variables

Check the function on the output of the sh ip int br command.
"""
from textfsm import clitable
from pprint import pprint


def parse_command_dynamic(
    command_output, attributes_dict, index_file="index", templ_path="templates"
):

    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    return [dict(zip(cli_table.header, row)) for row in cli_table]


if __name__ == "__main__":
    attributes = {"Command": "show ip int br", "Vendor": "cisco_ios"}
    with open("output/sh_ip_int_br.txt") as f:
        command_output = f.read()
    result = parse_command_dynamic(command_output, attributes)
    pprint(result, width=100)
