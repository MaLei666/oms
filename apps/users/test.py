#!/home/zkfr/.local/share/virtualenvs/xf-5EfV3Nly/bin/python
#-*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2019-05-30 21:40
# @file : test.py
# @software : PyCharm
import re
str1=str('40110300000005300400000000000703000000000001000BFE0001FFFFFFFFFFFF01025F23')
p = re.compile('.{1,2}')
print(' '.join(p.findall(str1)))