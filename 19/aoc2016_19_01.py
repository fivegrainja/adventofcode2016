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

parser = argparse.ArgumentParser()
parser.add_argument('num_elves', help='num_elves')
args = parser.parse_args()

num_elves = int(args.num_elves)
#
#    input_file = open(args.input_file)
#    input_lines = list(input_file.readlines())
#    input_file.close()


#test = True

#if test:
#    num_elves = 5
#else:
#    num_elves = 3004953
orig_num_elves = num_elves
elves = num_elves * [1]


def find_next(j):
    n = num_elves // 2
    while n:
        j = (j + 1) % orig_num_elves
        if elves[j]:
            n -= 1
    return j

def whose_turn(j):
    while True:
        j = (j+1) % orig_num_elves
        if elves[j]:
            return j

taking = 0
while num_elves > 1:
    #print(elves)
    take_from = find_next(taking)
    #print('taking: %s' % taking)
    #print('take_from: %s' % take_from)
    elves[taking] += elves[take_from]
    elves[take_from] = 0
    num_elves -= 1
    if num_elves % 10000 == 0:
        print('num: %s' % num_elves)
    taking = whose_turn(taking)

print(taking+1)












