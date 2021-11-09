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

    length = 0

    for line in input_lines:
        line = line.strip()
        # print('orig line is %s' % line)
        while True:
            open_parens = line.find('(')
            if open_parens > -1:
                # print('open_parens = %s' % open_parens)
                x = open_parens + line[open_parens:].find('x')
                # print('x = %s' % x)
                close_parens = line[x:].find(')')
                # print('close_parens = %s' % close_parens)
                num_chars = int(line[open_parens+1:x])
                # print('num_chars = %s' % num_chars)
                num_repeats = int(line[x+1:close_parens])
                # print('num_repeats = %s' % num_repeats)
                to_repeat = line[close_parens+1:close_parens+1+num_chars]
                # print('to_repeat = %s' % to_repeat)
                line = line[:open_parens] + ((num_repeats-1) * to_repeat) + line[close_parens+1:]
            else:
                line_length = len(line)
                # print('decompressed = %s' % line)
                # print('line length = %s' % line_length)
                length += line_length
                print('interim length = %s' % length)
                break
        # print()

    print('length = %s' % length)


