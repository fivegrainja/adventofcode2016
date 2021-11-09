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

#    parser = argparse.ArgumentParser()
#    parser.add_argument('input_file', help='File of input data')
#    args = parser.parse_args()
#
#    input_file = open(args.input_file)
#    input_lines = list(input_file.readlines())
#    input_file.close()


test = False

if test:
    num_elves = 5
else:
    num_elves = 3004953

counts = num_elves * [1]
positions = range(1, num_elves+1)
elves = collections.deque(zip(counts, positions))


taking = 0
while num_elves > 1:
    #print(elves)
    take_from = (taking + (num_elves // 2)) % num_elves
    #print('taking: %s' % taking)
    #print('take_from: %s' % take_from)
    elves[taking] = (elves[taking][0] + elves[take_from][0], elves[taking][1])
    del elves[take_from]
    num_elves -= 1
    if num_elves % 10000 == 0:
        print('num: %s' % num_elves)
    if take_from < taking:
        taking = taking % num_elves
    else:
        taking  = (taking + 1) % num_elves

print('%s has %s' % (elves[0][1], elves[0][0]))












