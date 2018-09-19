#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import collections

## i=1
# s="1"
# while i<10:
#     i+=1
# #     s="."+s
#     s+="." 
# print(s) 

# for x,y in ((1,1),(2,4),(3,9)):
#     print(x,y)

Sale=collections.namedtuple("Sale","productid customerid date quantity price")
sales=[]
sales.append(Sale(432,921,"2008-09-14",3,7.99))
sales.append(Sale(419,874,"2008-09-15",1,18.49))
