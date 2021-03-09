# -*- coding: utf-8 -*-
"""
Task 11.1

Create a function parse_cdp_neighbors that handles
show cdp neighbors command output.

The function must have one parameter, command_output, which expects a single
string of command output as an argument (not a filename). To do this, you need
to read the entire contents of the file into a string, and then pass the string
as an argument to the function (how to pass the command output is shown in the code below).

The function should return a dictionary that describes the connections between devices.


For example, if the following output was passed as an argument:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

The function should return a dictionary:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

In the dictionary, interfaces must be written without a space between type and name.
That is, so Fa0/0, and not so Fa 0/0.

Check the operation of the function on the contents of the sh_cdp_n_sw1.txt file.
In this case, the function should work on other files (the test checks the operation
of the function on the output from sh_cdp_n_sw1.txt and sh_cdp_n_r3.txt).

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""


def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    result = {}
    for line in command_output.split("\n"):
        line = line.strip()
        columns = line.split()
        if ">" in line:
            hostname = line.split(">")[0]
        # 3 индекс это столбец holdtime - там всегда число
        elif len(columns) >= 5 and columns[3].isdigit():
            r_host, l_int, l_int_num, *other, r_int, r_int_num = columns
            result[(hostname, l_int + l_int_num)] = (r_host, r_int + r_int_num)
    return result


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
