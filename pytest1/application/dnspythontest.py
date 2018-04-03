#!/usr/bin/env python
#Author:TangHu
from __future__ import print_function
import dns.resolver
data = dns.resolver.query('www.hnjtjh.com','A')
for item in data.response.answer:
    print(item)