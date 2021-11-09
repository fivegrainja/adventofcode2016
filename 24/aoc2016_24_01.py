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
from pprint import pprint


from implementation import *

#def breadth_first_search_1(graph, start, goal):
#    # print out what we find
#    frontier = Queue()
#    frontier.put(start)
#    visited = {}
#    visited[start] = True
#    steps = 0
#    print('bfs with start=%s and goal=%s' % (start, goal))
#    while not frontier.empty():
#        current = frontier.get()
#        #if current is None:
#        #    print('Current is None')
#        #print('current is %s' % str(current))
#        if current == goal:
#            print('returning %s' % steps)
#            return steps
#        steps += 1
#        print("Visiting %r" % str(current))
#        for next in graph.neighbors(current):
#            print('adding neighbor %s' % str(next))
#            if next not in visited:
#                frontier.put(next)
#                visited[next] = True
#    return None

def breadth_first_search_3(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    return came_from

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file')
args = parser.parse_args()

class MyGrid(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def cost(self, from_node, to_node):
        return 1

def calc_costs():

    input_file = open(args.input_file)
    input_lines = list(input_file.readlines())
    input_file.close()
    input_lines = [l.strip() for l in input_lines]

    # Build graph
    width = len(input_lines[0])
    height = len(input_lines)
    g = MyGrid(width, height)
    goals = {}
    for row, line in enumerate(input_lines):
        for col, c in enumerate(line):
            if c.isdigit():
                goals[int(c)] = (col, row)
            elif c == '#':
                g.walls.append((col, row))

    #pprint(g.walls)
    #print('goals:')
    #pprint(goals)
    # Get shortest paths

    shortest_paths = {}
    for x in range(len(goals)):
        for y in range(x+1, len(goals)):
            # Find shortest path from x to y
            #print('bfs on %s %s' % (goals[x], goals[y]))
            came_from, cost_so_far = dijkstra_search(g, goals[x], goals[y])
            path = reconstruct_path(came_from, goals[x], goals[y])
            #print('path is %s' % path)
            length = len(path) - 2
            shortest_paths['%s%s' % (x, y)] = length

    #pprint(goals)
    #print()
    pprint(shortest_paths)


#print(calc_costs())
costs = {'01': 26,
 '02': 206,
 '03': 184,
 '04': 180,
 '05': 160,
 '06': 96,
 '07': 60,
 '12': 216,
 '13': 194,
 '14': 190,
 '15': 170,
 '16': 98,
 '17': 58,
 '23': 34,
 '24': 62,
 '25': 98,
 '26': 290,
 '27': 250,
 '34': 48,
 '35': 80,
 '36': 268,
 '37': 228,
 '45': 44,
 '46': 264,
 '47': 224,
 '56': 240,
 '57': 204,
 '67': 68}

#costs = {
# '01': 2,
# '02': 8,
# '03': 10,
# '04': 2,
# '12': 6,
# '13': 8,
# '14': 4,
# '23': 2,
# '24': 10,
# '34': 8}

paths = ['0' + ''.join(p) for p in itertools.permutations('1234567', 7)]
#paths = ['0'+''.join(p) for p in itertools.permutations('1234', 4)]
#print(paths)

lowest_cost = None
lowest_path = None
for p in paths:
    #print('calculating cost for path %s' % p)
    cost = 0
    for i in range(len(p)-1):
        pair = '%s%s' % (min(p[i], p[i+1]), max(p[i], p[i+1]))
        cost += costs[pair]
        #print('-cost for pair %s is %s' % (pair, costs[pair]))
    #print('Cost of %s is %s' % (p, cost))
    if lowest_cost is None or cost < lowest_cost:
        lowest_cost = cost
        lowest_path = p

print('lowest cost: %s' % lowest_cost)
print('lowest path: %s' % lowest_path)




