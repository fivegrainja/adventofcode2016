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
    'a': 7,
    'b': 0,
    'c': 1,
    'd': 0
}


def get_value(x):
    if x in 'abcd':
        return registers[x]
    return int(x)


def execute(input_lines, command_pointer):
    line = input_lines[command_pointer]
    #print('line %s: %s' % (command_pointer, line))
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
    elif cmd == 'tgl':
        line_offset = get_value(parts[1])
        tgt_command_pointer = command_pointer + line_offset
        if 4 <= tgt_command_pointer <= 9:
            raise Exception('gah')
        if 0 <= tgt_command_pointer < len(input_lines):
            tgt_line = input_lines[command_pointer+line_offset]
            tgt_parts = tgt_line.split()
            tgt_cmd = tgt_parts[0]
            if tgt_cmd == 'inc':
                new_cmd = 'dec %s' % tgt_parts[1]
            elif tgt_cmd in ('dec', 'tgl'):
                new_cmd = 'inc %s' % tgt_parts[1]
            elif tgt_cmd == 'jnz':
                new_cmd = 'cpy %s %s' % (tgt_parts[1], tgt_parts[2])
            elif tgt_cmd in ('cpy'):
                new_cmd = 'jnz %s %s' % (tgt_parts[1], tgt_parts[2])
            else:
                raise Exception('missed something %s' % tgt_line)
            input_lines[command_pointer+line_offset] = new_cmd


    return result


command_pointer = 0
num_lines = len(input_lines)
while command_pointer < num_lines:
    command_pointer += execute(input_lines, command_pointer)
    #print(sorted(list(registers.items())))
print('a: %s' % registers['a'])
















