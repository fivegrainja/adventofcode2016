#! /usr/local/bin/python3

import argparse
import string
import collections
import hashlib

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='File of input data')
    args = parser.parse_args()

    input_file = open(args.input_file)
    input_lines = input_file.readlines()
    input_file.close()

    def get_length(s):
        # print('get_length of %s' % s)
        open_parens = s.find('(')
        if open_parens == -1:
            return len(s)
        # print('open parens = %s' % open_parens)
        x = open_parens + s[open_parens:].find('x')
        # print('x = %s' % x)
        close_parens = x + s[x:].find(')')
        # print('close parens = %s' % close_parens)
        num_chars = int(s[open_parens+1:x])
        # print('num chars = %s' % num_chars)
        num_repeats = int(s[x+1:close_parens])
        # print('num repeats = %s' % num_repeats)
        to_repeat = s[close_parens+1:close_parens+1+num_chars]
        # print('to repeat = %s' % to_repeat)
        if num_repeats > 0:
            num_repeats -= 1
        return open_parens + (num_repeats * get_length(to_repeat)) + get_length(s[close_parens+1:])

    length = 0

    for line in input_lines:
        length += get_length(line)

    print('length = %s' % length)


