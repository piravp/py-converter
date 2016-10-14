#
# Created: 06.10.16
#

import os
import re


def findAndReplace(s):

    # substitute with regular expression
    new_s = re.sub("print\s*", "print(", s)

    # only add last bracket if first bracket was detected
    if new_s != s:
        # get last character in line
        c = new_s[-2:]
        # strip any whitespace character, add bracket
        c = c.strip()
        c+=")"

        # replace last character
        new_s = re.sub(".$", c, new_s)
        return new_s

    # return original string if nothing was changed
    return s



def convert(file_name, converted_file="convertedfile.py"):
    """
    :param file_name: python 2.x file
    :param converted_file: name of new python 3.x file
    """

    # check if file is a python file
    if not file_name.endswith(".py"):
        print("This is not a python file.")
        return

    with open(file_name, "r") as f:

        # delete file if already exists
        if os.path.isfile(converted_file):
            os.system("del %s" % converted_file)
            print("%s was overwritten." % converted_file)


        for line in f:
            new_file = open(converted_file, "a")
            # line = line.replace("hello", "haalla")
            line = findAndReplace(line)
            new_file.write(line)

#file = r"tfile.py"
#convert(file)