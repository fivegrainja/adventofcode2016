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
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

max_val = 4294967295

spans = []
for line in input_lines:
    parts = line.split('-')
    start = int(parts[0])
    end = int(parts[1])
    spans.append((start, end))
spans.sort()

n = max(0, spans[0][0])
end = 0
for i in range(len(spans)-1):
    end = max(end, spans[i][1])
    next_start = spans[i+1][0]
    if end + 1 < next_start:
        n += next_start - end - 1

print(n)


