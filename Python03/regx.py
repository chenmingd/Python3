#! /usr/bin/env python3
#-*- coding:utf-8 -*-
import re
email=re.match(r'^\w+[_|\.]?\w+@\w+\.\w+$',"someone@gmail.com")
print(email)
#email=re.match(r'^\w+[_|\.]?\w+@\w+\.\w+$',"bill.gates@microsoft.com")
email=re.match(r'^[a-zA-Z][a-zA-Z\_\.]+@\w+\.\w+$',"bill.gates@microsoft.com")
print(email)
email=re.match(r'<[\w|\s]+>\s*([a-zA-Z][a-zA-Z\_\.]+@\w+\.\w+)','<Tom Paris> tom@voyager.org')
print(email)
print(email.groups()[0])
