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
    input = 'ulqzkmiv'
else:
    input = 'mmsxrhfx'


states = [(0, 0, input)]  # [((x,y), path)]

open_doors = 'bcdef'

longest = ''

def process_states(states):
    global longest
    new_states = []
    for state in states:
        if state[0:2] == (3, 3):
            path = state[2][len(input):]
            if len(path) > len(longest):
                longest = path
            continue 
        hash = hashlib.md5(bytes(state[2], 'utf-8')).hexdigest()
        # Up
        if state[1] > 0 and hash[0] in open_doors:
            new_states.append((state[0], state[1]-1, state[2]+'U'))
        # Down
        if state[1] < 3 and hash[1] in open_doors:
            new_states.append((state[0], state[1]+1, state[2]+'D'))
        # Left
        if state[0] > 0 and hash[2] in open_doors:
            new_states.append((state[0]-1, state[1], state[2]+'L'))
        # Right
        if state[0] < 3 and hash[3] in open_doors:
            new_states.append((state[0]+1, state[1], state[2]+'R'))
    if new_states:
        process_states(new_states)


state = process_states(states)
print(longest)
print(len(longest))

















