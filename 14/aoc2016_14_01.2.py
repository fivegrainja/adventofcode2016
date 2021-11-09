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
# m = hashlib.md5()
# b = bytearray(door_id + str(i), 'utf-8')
# m.update(b)
# digest = m.hexdigest()


test_data = False

if test_data:
    salt = 'abc'
else:
    salt = 'ngcjuoqr'

goal = 64
regex = re.compile(r'([abcdef0-9])\1{2}')

def go():
    hashes = []
    for i in range(50000):
        b = bytearray(salt + str(i), 'utf-8')
        m = hashlib.md5()
        m.update(b)
        hash = m.hexdigest()
        hashes.append(hash)

    i = 0
    keys = []
    while len(keys) < goal:

        # Does this have a 3 seq?
        hash = hashlib.md5(s.encode('utf-8')).hexdigest()
        g = re.search(regex, hash)
        if g:
            validate = g.group()[0] * 5
            if any(validate in hashes[h] for h in range(i+1, i+1001)):
                keys.append(hash)
        i += 1












