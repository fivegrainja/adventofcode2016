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
# m = hashlib.md5()
# b = bytearray(door_id + str(i), 'utf-8')
# m.update(b)
# digest = m.hexdigest()


test_data = False

if test_data:
    salt = 'abc'
else:
    salt = 'ngcjuoqr'

goal = 64


candidates = collections.defaultdict(list)
keys = []  # (key, when found)

i = 0
while len(keys) < goal:

    # Generate hash
    b = bytearray(salt + str(i), 'utf-8')
    m = hashlib.md5()
    m.update(b)
    hash = m.hexdigest()

    # PROBLEM - consider only the fist triple, not folling ones.
    # Maybe consider more than first 5-sequence though
    is_first_triple = True
    for k, g in itertools.groupby(hash):
        g = ''.join(list(g))

        # Does it contain any 5 sequences?
        if len(g) >= 5:
            key = ''.join(g[:3])
            for line_num in candidates[key]:
                print('saw %s in line %s' % (key, line_num))
                if line_num + 1000 >= i:
                    print('adding %s to keys' % key)
                    keys.append((key, line_num))
            # everything in the list is either too old or just got matched (and don't want to match again)
            del candidates[key]

        # Question - does an unmatched 5 sequence count as a new potential keys? Assume yes for now.

        if len(g) >= 3 and is_first_triple:
            print('adding potential key %s from line %s' % (g, i))
            candidates[g].append(i)
            is_first_triple = False

    i += 1

keys.sort(key=lambda x: x[1])

print('i: %s' % i)
print('num keys: %s' % len(keys))
print('keys is %s' % keys)






#
#    # Get repeated sequence
#    key = get_repeated_character(hash)
#
#    # If repeated sequence:
#    if key:
#        potential_match = key[:3]
#        print('found potential key %s at %s' % (potential_match, i))
#        if len(key) >= 5:
#            print('potential match %s at %s' % (potential_match, i))
#            print('in potential_keys: %s' % (potential_match in potential_keys))
#            if i == 816:
#                print('potential_keys is %s' % potential_keys)
#            if potential_match in potential_keys:
#                lines = potential_keys[potential_match]
#                for line in lines:
#                    if line + 1000 >= i:
#                        print('found actual key %s at %s' % (potential_match, i))
#                        keys.append((potential_match, line))
#                else:
#                    potential_keys[potential_match].append(i)
#            else:
#                potential_keys[potential_match].append(i)
#    i += 1
#
#
#print('potentials keys %s' % potential_keys)
#print('keys is %s' % keys)
#print('final match on line %s' % keys[-1][1])
#
#











