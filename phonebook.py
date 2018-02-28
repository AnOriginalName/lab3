#!/usr/bin/env python

import sys
import os

PHONEBOOK_ENTRIES = "python_phonebook_entries"


def main():
    if len(sys.argv) < 2:
         print("INVALID ARGS")
         exit(1)
    elif sys.argv[1] == "new":
        
        if os.path.isfile(PHONEBOOK_ENTRIES):
            f = open(PHONEBOOK_ENTRIES, 'a')
        else:
            f = open(PHONEBOOK_ENTRIES, 'w')
        f.write(" ".join(sys.argv[2:]) + "\n")
        f.close()
    elif sys.argv[1] == "list":

        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            with open(PHONEBOOK_ENTRIES, 'r') as f:
                print(f.read())
                f.close()
    elif sys.argv[1] == "remove":
        name = " ".join(sys.argv[2:])
        f = open(PHONEBOOK_ENTRIES, 'r') 
        
        result = ""
        for line in f:
            if not (name in line):
                result += line
        f.close()
        f = open(PHONEBOOK_ENTRIES,'w')
        f.write(result)
        f.close()
    elif sys.argv[1] == "clear":
        if os.path.isfile(PHONEBOOK_ENTRIES):
            remove(PHONEBOOK_ENTRIES)
    else:
        name = " ".join(sys.argv[1:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lookup = "".join(filter(lambda line: name in line, f.readlines()))
if __name__ == "__main__":
    main()
