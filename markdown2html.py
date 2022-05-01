#!/usr/bin/python3

"""
Converting Markdown script using python.
"""
import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
                file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1], "r") as readme:
        text, tmp = "", ""
        text_ant = "\n"
        my_list, other = [], []
        simbols = ["-", "*", " ", "#"]

        for line in readme.readlines():
            count = 0
            while line.find("**") != -1 or line.find("__") != -1:
                line = line.replace("**", "<b>", 1)
                line = line.replace("**", "</b>", 1)
                line = line.replace("__", "<em>", 1)
                line = line.replace("__", "</em>", 1)
            while line.find("[[") != -1 and line.find("]]") != -1:
                start = line.index("[[") + 2
                end = line.index("]]")
                new_hash = line[start:end]
                hash_md = hashlib.md5(new_hash.encode("utf")).hexdigest()
                line = line.replace(new_hash, hash_md)
                line = line.replace("[[", "", 1)
                line = line.replace("]]", "", 1)
            while line.find("((") != -1 and line.find("))") != -1:
                start = line.index("((") + 2
                end = line.index("))")
                remove = line[start:end]
                remove1 = remove.replace("c", "")
                remove1 = remove1.replace("C", "")
                line = line.replace(remove, remove1)
                line = line.replace("((", "", 1)
                line = line.replace("))", "", 1)
            for caracter in line:
                if caracter not in simbols:
                    my_list = []
                    if caracter == "\n":
                        text_ant = caracter
                        break
                    if text_ant == "\n":
                        tmp = text
                        text += "<p>\n{}</p>\n".format(line)
                    else:
                        text = tmp
