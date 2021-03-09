# -*- coding: utf-8 -*-
"""
Task 21.1

Create parse_command_output function. Function parameters:
* template - name of the file containing the TextFSM template.
  For example templates/sh_ip_int_br.template
* command_output - output the corresponding show command (string)

The function should return a list:
* the first element is a list with column names
* the rest of the items are lists, which contain the results
  of processing the output of the show command

Check the operation of the function on the output of the sh ip int br command
from the equipment and on the templates/sh_ip_int_br.template template.

"""
import textfsm


def parse_command_output(template, command_output):
    with open(template) as tmpl:
        parser = textfsm.TextFSM(tmpl)
        header = parser.header
        result = parser.ParseText(command_output)
    return [header] + result


if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt") as show:
        output = show.read()
    result = parse_command_output("templates/sh_ip_int_br.template", output)
    print(result)
