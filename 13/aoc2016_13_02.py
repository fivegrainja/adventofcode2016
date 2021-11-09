#! /usr/local/bin/python3

import argparse
import string
import collections
import hashlib
from pprint import pprint

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
# m = hashlib.md5()
# b = bytearray(door_id + str(i), 'utf-8')
# m.update(b)
# digest = m.hexdigest()

test_data = False

# x*x + 3*x + 2*x*y + y + y*y

if test_data:
    input = 10
    dimension = 15
else:
    input = 1364
    dimension = 51

start = (0, 0)


map = []
for x in range(dimension):
    col = []
    map.append(col)
    for y in range(dimension):
        num = x*x + 3*x + 2*x*y + y + y*y
        num += input
        bnum = bin(num)[2:]
        num_bits = 0
        for i in bnum:
            num_bits += int(i)
        if num_bits % 2 == 0:
            col.append(1)
        else:
            col.append(0)

#pprint(map)


def get_neighbors(loc):
    x, y = loc
    neighbors = set()
    for dx in [-1, 1]:
        new_x = x + dx
        #print('considering %s,%s' % (new_x, y))
        #print('map there is %s' % map[new_x][y])
        if 0 <= new_x < dimension and map[new_x][y]:
            neighbors.add((new_x, y))
    for dy in [-1, 1]:
        new_y = y + dy
        #print('considering %s,%s' % (x, new_y))
        #print('map there is %s' % map[x][new_y])
        if 0 <= new_y < dimension and map[x][new_y]:
            neighbors.add((x, new_y))
    return neighbors


def check_then_visit_neighbors(locations, step, visited):
    if not locations:
        raise Exception('Did not find solution by step %s' % step)
    for loc in locations:
        visited.add(loc)
    if step == 49:
        return len(visited)
    neighbors = set()
    for loc in locations:
        loc_neighbors = get_neighbors(loc)
        neighbors |= loc_neighbors
    new_neighbors = set([n for n in neighbors if n not in visited])
    return check_then_visit_neighbors(new_neighbors, step+1, visited)

min_steps = check_then_visit_neighbors(set([start]), 0, set())

print('visited: %s' % min_steps)










