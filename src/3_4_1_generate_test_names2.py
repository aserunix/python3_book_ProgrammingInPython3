#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

limit = 100
years=list(range(1970,2013))*3
for year,forename,surname in zip(random.sample(year,limit),
                                 random.sample(forename,limit),
                                 random.sample(surnames.limit)):
    name="{0} {1}".format(forename,surname)
fh.write("{0:.<25}.{1}\n".format(name,year))
