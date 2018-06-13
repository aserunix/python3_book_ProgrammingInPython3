#! /usr/bin/env python3
# -*- coding=utf-8 -*-

if __name__=="__main__":
  s=input("enter an interger:")
  try:
    i=int(s)
    print("valid integer entered:",i)
  except ValueError as err:
    print(err)