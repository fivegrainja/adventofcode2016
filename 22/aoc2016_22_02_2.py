#! /usr/local/bin/python3

import sys
import argparse
import string
import collections
import hashlib
import re
import itertools
import sympy
import numpy
import llist
import heapq
from pprint import pprint
import copy

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

y_dimension = 30
x_dimension = 32

# Filesystem              Size  Used  Avail  Use%

with open(args.input_file) as f:
    input_lines = list(f.readlines())

Node = collections.namedtuple('Node', 'row col size used avail')
State = collections.namedtuple('State', 'rows g_row g_col')

#def tuplify_state(state):
#    new_state = State(
#        tuple(tuple(r) for r in state.rows),
#        state.g_row,
#        state.g_col
#        )
#    return new_state
#
#def listify_state(state):
#    state.rows = list(state.rows)
#    for row_num in range(dimension):
#        state.rows[row_num] = list(state.rows[row_num])
#    return state

rows = []
for r in range(y_dimension+1):
    rows.append((x_dimension+1) * [None])

for line in input_lines:
    parts_x = line.split('-')
    print('parts_x is %s' % parts_x)
    col = int(parts_x[1][1:])
    print('col is %s' % col)
    row = int(parts_x[2].split()[0][1:])
    print('row is %s' % row)
    parts = line.split()
    rows[row][col] = Node(row, col, int(parts[1][:-1]), int(parts[2][:-1]), int(parts[3][:-1]))

#for row_num in range(dimension):
#    for col_num in range(dimension):
#        line = input_lines[col_num*dimension+row_num]
#        parts = line.split()
#        rows[row_num][col_num] = Node(row_num, col_num, int(parts[1][:-1]), int(parts[2][:-1]), int(parts[3][:-1]))
init_state = State(tuple(tuple(r) for r in rows), 0, x_dimension-1)


#pprint(init_state)
#print()

def print_state(state):

    print('                           1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3')
    print('       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2')
    for row_num, row in enumerate(state.rows):
        print('row %2s' % row_num, end=' ')
        for node in row:
            if node is None:
                print('X', end=' ')
            elif node.row == state.g_row and node.col == state.g_col:
                print('G', end=' ')
            elif node.used == 0:
                print('_', end=' ')
            elif node.used/node.size > 0.9:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print(' row %2s' % row_num)
    print('       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2')
    print('                           1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3')

print_state(init_state)



