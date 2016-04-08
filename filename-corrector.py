#!/usr/sbin/env python
#### FileName: filename_correcter.py
#### Description: Correct missing filenames.
#### FeedBack: Vahid.Maani@gmail.com
#### Weblog: gnutips.ir

#--|Imported Modules
import os
import sys
import string

#--|Functions

def renamer(old_name):
    new_name = old_name.replace(" ","-")
    os.rename(old_name, new_name)
    return new_name

def should_rename(old_name):
    uchar = " "
    if uchar in old_name:
            return True
    return False

def parser(path):
    print("\t\tGooing==>",path)
    os.chdir(path)
    for dirpath, dirname, filename in os.walk('.'):
        for dir_name in dirname:
            print("\tselect =>",dir_name)
            tmp = dir_name
            if should_rename(dir_name):
                tmp = renamer(dir_name)
                print("\trenamed to =>",tmp)
            parser(tmp)
            os.chdir('..')
            print("here ", os.getcwd())
        for file_name in filename:
            print("\tselect =>",file_name)
            if should_rename(file_name):
                tmp2 = renamer(file_name)
                print("\trenamed to",tmp2)
        return(0)

#--|Main

#notify2.init("icon-summary-body")
parser(sys.argv[1])
