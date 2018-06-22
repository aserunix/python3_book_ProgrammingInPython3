#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

word=None
if len(sys.argv)>1:
    if sys.argv[1] in ("-h","--help"):
        print("usage:{0}[string]".format(sys.argv[0]))
        word=0
    else:
        word=sys.argv[1].lower()

if word !=0:
    print_unicode_table(word)
    
    