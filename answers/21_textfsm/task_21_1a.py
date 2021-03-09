# -*- coding: utf-8 -*-
"""
Task 21.1a

Create parse_output_to_dict function.

Function parameters:
* template is the name of the file containing the TextFSM template.
  For example templates/sh_ip_int_br.template
* command_output - output of the corresponding show command (string)

The function should return a list of dictionaries:
* keys - names of variables in the TextFSM template
* values - parts of the output that correspond to variables

Check the operation of the function on the output of the command
output/sh_ip_int_br.txt and the template templates/sh_ip_int_br.template.
"""
from pprint import pprint
import textfsm


def parse_output_to_dict(template, command_output):
    with open(template) as tmpl:
        parser = textfsm.TextFSM(tmpl)
        header = parser.header
        result = parser.ParseText(command_output)
    return [dict(zip(parser.header, line)) for line in result]


if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt") as show:
        output = show.read()
    result = parse_output_to_dict("templates/sh_ip_int_br.template", output)
    pprint(result, width=100)


# ParseTextToDicts version
def parse_output_to_dict(template, command_output):
    with open(template) as template:
        fsm = textfsm.TextFSM(template)
        result = fsm.ParseTextToDicts(command_output)
    return result
