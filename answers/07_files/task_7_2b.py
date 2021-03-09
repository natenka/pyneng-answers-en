# -*- coding: utf-8 -*-
"""
Task 7.2b

Make a copy of the code from the task 7.2a.
Add this functionality: instead of printing to stdout,
the script should write the resulting lines to a file.

File names must be passed as arguments to the script:
  1. name of the source configuration file
  2. name of the destination configuration file

In this case, the lines that are contained in the ignore list and lines
that start with ! must be filtered.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
from sys import argv

ignore = ["duplex", "alias", "configuration"]

src_file, dst_file = argv[1], argv[2]

with open(src_file) as src, open(dst_file, 'w') as dst:
    for line in src:
        words = line.split()
        words_intersect = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersect:
            dst.write(line)
