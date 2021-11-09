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

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

input = 'fbgdceah'

# swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
# swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
# rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
# rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
# reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
# move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.

input = collections.deque(input)
index = collections.deque('01234567')

for line in input_lines[::-1]:
    parts = line.split()
    print()
    print('line is %s' % line.strip())
    print('index is %s' % index)
    print('input is %s' % input)
    if line.startswith('swap position'):
        x = int(parts[2])
        y = int(parts[5])
        c = input[x]
        input[x] = input[y]
        input[y] = c
    elif line.startswith('swap letter'):
        x_pos = input.index(parts[2])
        y_pos = input.index(parts[5])
        input[x_pos] = parts[5]
        input[y_pos] = parts[2]
    elif line.startswith('rotate left'):
        num = int(parts[2])
        input.rotate(num)
    elif line.startswith('rotate right'):
        num = -int(parts[2])
        input.rotate(num)
    elif line.startswith('rotate based'):
        c = parts[6]
        cur_pos = input.index(c)
        #print('- c is %s' % c)
        #print('- cur_pos is %s' % cur_pos)
        for i in range(len(input)):
            potential = input.copy()
            potential.rotate(-i)
            #print('- potential is %s' % potential)
            new_pos = potential.index(c)
            if new_pos >= 4:
                new_pos += 1
            new_pos += 1
            #print('- new_pos is %s' % new_pos)
            #print('- i is %s' % i)
            #print()
            if i == new_pos % len(input):
                break
        else:
            raise Exception('did not work')
            #print('- potential is %s' % potential)
            #print('- new_pos is %s' % new_pos)
            #if new_pos % len(input) == cur_pos:
            #    break
        input.rotate(-i)
        #pos = input.index(parts[6])
        #if pos >= 4:
        #   pos += 1
        #pos += 1
        #print('pos is %s' % pos)
        #input.rotate(pos)
    elif line.startswith('reverse'):
        x_pos = int(parts[2])
        y_pos = int(parts[4])
        s = list(input)[x_pos:y_pos+1][::-1]
        #print('x_pos is %s' % x_pos)
        #print('y_pos is %s' % y_pos)
        #print('s is %s' % s)
        for i in range(len(s)):
            input[x_pos+i] = s[i]
    elif line.startswith('move'):
        y = int(parts[2])
        x = int(parts[5])
        input.rotate(-x)
        c = input.popleft()
        input.rotate(x)
        input.insert(y, c)
    else:
        raise Exception('Bad command: %s' % line)
    

print(''.join(input))














