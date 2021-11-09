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


    decompressed = ''
    for line in input_lines:
        line = line.strip()
        print('line is %s' % line)
        i = 0
        while True:
            print('i = %s' % i)
            print('looking for open paren in %s' % line[i:])
            open_parens = line[i:].find('(')
            if open_parens > -1:
                open_parens += i
                print('open_parens = %s' % open_parens)
                x = open_parens + line[open_parens:].find('x')
                print('x = %s' % x)
                close_parens = x + line[x:].find(')')
                print('close_parens = %s' % close_parens)
                num_chars = int(line[open_parens+1:x])
                print('num_chars = %s' % num_chars)
                num_repeats = int(line[x+1:close_parens])
                print('num_repeats = %s' % num_repeats)
                to_repeat = line[close_parens+1:close_parens+1+num_chars]
                print('to_repeat = %s' % to_repeat)
                decompressed += line[i:open_parens]
                decompressed += num_repeats * to_repeat
                i = close_parens + 1 + num_chars
            else:
                decompressed += line[i:]
                decompressed += '\n'
                break
        print()

    print('decompressd = \n%s' % decompressed)
    decompressed = decompressed.replace('\n', '').replace(' ', '')
    print('length without whitespace = %s' % len(decompressed))


