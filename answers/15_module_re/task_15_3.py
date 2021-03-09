# -*- coding: utf-8 -*-
"""
Task 15.3

Create a convert_ios_nat_to_asa function that converts NAT rules from
cisco IOS syntax to cisco ASA.

The function expects such arguments:
- the name of the file containing the Cisco IOS NAT rules
- the name of the file in which to write the NAT rules for the ASA

The function returns None.

Check the function on the cisco_nat_config.txt file.

Example cisco IOS NAT rules
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

And the corresponding NAT rules for the ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

In the file with the rules for the ASA:
- there should be no blank lines between the rules
- there must be no spaces before the lines "object network"
- there must be one space before the rest of the lines

In all rules for ASA, the interfaces will be the same (inside, outside).
"""
import re


def convert_ios_nat_to_asa(cisco_ios, cisco_asa):
    regex = (
        "tcp (?P<local_ip>\S+) +(?P<lport>\d+) +interface +\S+ (?P<outside_port>\d+)"
    )
    asa_template = (
        "object network LOCAL_{local_ip}\n"
        " host {local_ip}\n"
        " nat (inside,outside) static interface service tcp {lport} {outside_port}\n"
    )
    with open(cisco_ios) as f, open(cisco_asa, "w") as asa_nat_cfg:
        data = re.finditer(regex, f.read())
        for match in data:
            asa_nat_cfg.write(asa_template.format(**match.groupdict()))


if __name__ == "__main__":
    convert_ios_nat_to_asa("cisco_nat_config.txt", "cisco_asa_config.txt")
