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

dimension = 3

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
for row_num in range(dimension):
    row = []
    rows.append(row)
    for col_num in range(dimension):
        line = input_lines[row_num*dimension+col_num]
        parts = line.split()
        row.append(Node(row_num, col_num, int(parts[1][:-1]), int(parts[2][:-1]), int(parts[3][:-1])))
init_state = State(tuple(tuple(r) for r in rows), 0, dimension-1)


def get_viable_moves(state):
    # Returns list of tuples (src, dest) node pairs
    viable = []
    for row_num in range(dimension):
        for col_num in range(dimension):
            node_a = state.rows[row_num][col_num]
            if node_a.used > 0:
                # Upper
                if row_num > 0:
                    neighbor = state.rows[row_num-1][col_num]
                    if neighbor.avail >= node_a.used:
                        viable.append((node_a, neighbor))
                # Lower
                if row_num < dimension-1:
                    neighbor = state.rows[row_num+1][col_num]
                    if neighbor.avail >= node_a.used:
                        viable.append((node_a, neighbor))
                # Left
                if col_num > 0:
                    neighbor = state.rows[row_num][col_num-1]
                    if neighbor.avail >= node_a.used:
                        viable.append((node_a, neighbor))
                # Right
                if col_num < dimension-1:
                    neighbor = state.rows[row_num][col_num+1]
                    if neighbor.avail >= node_a.used:
                        viable.append((node_a, neighbor))
    #print('get_viable_moves returning %s' % len(viable))
    return viable


def get_state_for_move(state, move):  # Move is tuple of (src, dest) nodes
    # Concerned about performance of this copy
    node_a = state.rows[move[0].row][move[0].col]
    node_b = state.rows[move[1].row][move[1].col]
    # Node: row col size used avail
    new_used = node_b.used + node_a.used
    new_avail = node_b.size - new_used
    rows = [list(r) for r in state.rows]
    rows[node_b.row][node_b.col] = Node(node_b.row, node_b.col, node_b.size, new_used, new_avail)
    rows[node_a.row][node_a.col] = Node(node_a.row, node_a.col, node_a.size, 0, node_a.size)
    if node_a.row == state.g_row and node_a.col == state.g_col:
        g_row = node_b.row
        g_col = node_b.col
    else:
        g_row = state.g_row
        g_col = state.g_col
    return State(tuple(tuple(r) for r in rows), g_row, g_col)


def get_neighbors(state):
    moves = get_viable_moves(state)
    print('Moves:')
    pprint(moves)
    neighbor_states = []
    for move in moves:
        neighbor_states.append(get_state_for_move(state, move))
    #print('get_neighbors returning %s' % len(neighbor_states))
    print('Neighbors:')
    pprint(neighbor_states)
    sys.exit(1)
    return neighbor_states


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(state):
    # Primarily interested in closeness of goal to 0,0
    distance = state.g_row + state.g_col
    return distance

def get_cost(current, next):
    return 1

def a_star_search(start):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    loops = 0
    while not frontier.empty():
        loops += 1
        #print('num loops: %s' % loops)
        current = frontier.get()
        
        if current.g_col == 0 and current.g_row == 0:
            print('cost is %s' % cost_so_far(current))
            break
        
        for next in get_neighbors(current):
        #for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + get_cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far


came_from, cost_so_far = a_star_search(init_state)

#print('came_from')
#pprint(came_from)
#print()
#print('cost_so_far')
#pprint(cost_so_far)






