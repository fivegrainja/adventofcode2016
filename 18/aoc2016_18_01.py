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

#Then, a new tile is a trap only in one of the following situations:

#Its left and center tiles are traps, but its right tile is not.
#Its center and right tiles are traps, but its left tile is not.
#Only its left tile is a trap.
#Only its right tile is a trap.

traps = ('^^.', '.^^', '^..', '..^')

test_data = False

if test_data:
    input = '.^^.^.^^^^'
    num_rows = 10
else:
    input = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'
    num_rows = 400000


def get_next_row(row):
    next_row = []
    row = '.' + row + '.'
    #print('row=%s' % row)
    for i in range(1, len(row) - 1):
        #print('i=%s' % i)
        #print('considering: %s' % row[i-1:i+1])
        if row[i-1:i+2] in traps:
            next_row.append('^')
        else:
            next_row.append('.')
    return ''.join(next_row)

row = input
print(row)
num_safe = 0
for c in row:
    if c == '.':
        num_safe += 1

for i in range(num_rows-1):
    row = get_next_row(row)
    #print(row)
    for c in row:
        if c == '.':
            num_safe += 1

print(num_safe)















