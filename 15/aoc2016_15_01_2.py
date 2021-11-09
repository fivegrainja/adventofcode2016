#! /usr/local/bin/python3

import argparse
import string
import collections
import hashlib
import re
import itertools

# new_list = sorted(old_list, key=key_providing_function, reverse=False)
# self.compass = collections.deque(['N', 'E', 'S', 'W'])
#
# deque
# values = collections.deque()
# values.extend(col_1)
# values.extend(col_2)
#    while values:
#        a = values.popleft()
#        b = values.popleft()
#
# counter
# c = collections.Counter(name)
# common = sorted(c.most_common(), key=cmp_key, reverse=False)
#
# hashlib.md5(b"Nobody inspects the spammish repetition").hexdigest()
#
# @lru_cache(maxsize=None)
# def fib(n):
#
# >>> import re
# >>> m = re.search('(?<=abc)def', 'abcdef')
# >>> m.group(0)
# 'def'
 

test_data = False

if test_data:
    input = '1'
else:
    input = '11100010111110100'
    length = 272

# Call the data you have at this point "a".
# Make a copy of "a"; call this copy "b".
# Reverse the order of the characters in "b".
# In "b", replace all instances of 0 with 1 and all 1s with 0.
# The resulting data is "a", then a single 0, then "b".

a = input
while len(a) < 272:
    b = a[::-1]
    b = ['1' if c == '0' else '0' for c in b]
    a = a + '0' + b
a = a[:length]

check = collections.deque(a)
while len(check) % 2 == 0:
    new_check = ''
    while check:
        a = check.popleft()
        b = check.popleft()
        if a == b:
            new_check += '1'
        else:
            new_check += '0'
    check = new_check

print(check)























