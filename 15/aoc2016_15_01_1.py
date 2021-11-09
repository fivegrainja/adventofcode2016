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
    initial = [
        (5, 4),
        (2, 1)
    ]
else:
    initial = [
        (17, 1),
        (7, 0),
        (19, 2),
        (5, 0),
        (3, 0),
        #(13, 5)
        ]
discs = []

def initialize_discs():
    global discs
    discs[:] = []
    for state in initial:
        discs.append(collections.deque(state[0] * [0]))
        discs[-1][state[1]] = 1

def rotate_discs():
    global discs
    for disc in discs:
        disc.rotate(1)

start = 0
while True:
    print('Try starting at %s' % start)
    initialize_discs()
    for i in range(start):
        rotate_discs()
    for elapsed in range(1, len(discs) + 1):
        rotate_discs()
        print('elapsed: %s' % elapsed)
        print('discs: %s' % discs)
        print('discs[elapsed-1][0]: %s' % discs[elapsed-1][0])
        if not discs[elapsed-1][0]:
            print('Bounced away')
            break
    else:
        print('Works!  start at %s' % start)
        break
    start += 1
















