#! /usr/local/bin/python3

import argparse
import string
import collections
import hashlib
import re
import itertools
import sympy
import numpy
import llist

# c = collections.Counter(name)
# common = sorted(c.most_common(), key=cmp_key, reverse=False)
#
# hashlib.md5(b"Nobody inspects the spammish repetition").hexdigest()
#
# @lru_cache(maxsize=None) - decorator to memoize return values
#
# m = re.search('(?<=abc)def', 'abcdef')
# m.group(0)
#
# double_linked_list = llist.dllist(iterator)  - rotate, pop, append, appendright, nodeat
#
# Prime factorization
# from sympy.ntheory import factorint
# factorint(2000)    # 2000 = (2**4) * (5**3)
# {2: 4, 5: 3}

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

# Filesystem              Size  Used  Avail  Use%

with open(args.input_file) as f:
    input_lines = list(f.readlines())

Node = collections.namedtuple('Node', 'name size used avail use_percent')

nodes = collections.deque()
for line in input_lines:
    parts = line.split()
    nodes.append(Node(parts[0], int(parts[1][:-1]), int(parts[2][:-1]), int(parts[3][:-1]), int(parts[4][:-1])))

viable = []
for i in range(len(nodes)):
    node_a = nodes[i]
    if node_a.used > 0:
        for j in range(len(nodes)):
            if i != j:
                node_b = nodes[j]
                if node_a.used <= node_b.avail:
                    viable.append((node_a, node_b))

print(len(viable))







