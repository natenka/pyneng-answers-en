# -*- coding: utf-8 -*-
"""
Task 7.2a

Make a copy of the code from the task 7.2.

Add this functionality: The script should not print to the stdout commands,
which contain words from the ignore list.

The script should also not print lines that begin with !.

Check the script on the config_sw1.txt configuration file.
The filename is passed as an argument to the script.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
from sys import argv

ignore = ["duplex", "alias", "configuration"]

filename = argv[1]

with open(filename) as f:
    for line in f:
        words = line.split()
        words_intersect = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersect:
            print(line.rstrip())

