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

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='File of input data')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

registers = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}


def get_value(x):
    if x in 'abcd':
        return registers[x]
    return int(x)


def execute(line):
    # Return delta for line.
    # print('executing %s' % line)
    result = 1
    parts = line.split()
    cmd = parts[0]
    if cmd == 'cpy':
        registers[parts[2]] = get_value(parts[1])
    elif cmd == 'inc':
        registers[parts[1]] += 1
    elif cmd == 'dec':
        registers[parts[1]] -= 1
    elif cmd == 'jnz':
        if get_value(parts[1]) != 0:
            result = get_value(parts[2])
    return result


command_pointer = 0
num_lines = len(input_lines)
while command_pointer < num_lines:
    command_pointer += execute(input_lines[command_pointer])
print(registers)
















