#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

try:
    digits=sys.argv[1]
    row=0
    while row <7:
        line=""
        column=0
        while column <len(digits):
            number=int(digits[column])
            digits=Digits[number]
            line+=digit[row]+""
            column+=1     
        print(line)
        row+=1
except IndexError:
    print("usage:bigdigits.py<number>")
except ValueError:
    print(err,"in",digits)