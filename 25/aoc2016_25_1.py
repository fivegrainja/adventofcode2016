#! /usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='File of input data')
args = parser.parse_args()

input_file = open(args.input_file)
input_lines = list(input_file.readlines())
input_file.close()

registers = {}

def get_value(x):
    if x in 'abcd':
        return registers[x]
    return int(x)


def execute(input_lines, command_pointer, signal):
    line = input_lines[command_pointer]
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
    elif cmd == 'out':
        signal.append(str(get_value(parts[1])))
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
            elif tgt_cmd in ('dec', 'tgl', 'out'):
                new_cmd = 'inc %s' % tgt_parts[1]
            elif tgt_cmd == 'jnz':
                new_cmd = 'cpy %s %s' % (tgt_parts[1], tgt_parts[2])
            elif tgt_cmd in ('cpy'):
                new_cmd = 'jnz %s %s' % (tgt_parts[1], tgt_parts[2])
            else:
                raise Exception('missed something %s' % tgt_line)
            input_lines[command_pointer+line_offset] = new_cmd


    return result


def generate_signal(posint, length):
    global registers
    registers = {
        'a': int(posint),
        'b': 0,
        'c': 0,
        'd': 0
    }
    command_pointer = 0
    num_lines = len(input_lines)
    signal = []
    while command_pointer < num_lines:
        command_pointer += execute(input_lines, command_pointer, signal)
        if len(signal) >= length:
            return signal
    return ''

for i in range(1,1000):
    signal = generate_signal(i, 10)
    print('i=%s signal=%s' % (i, signal))
    sig = ''.join(signal)
    if sig.startswith('1010101010') or sig.startswith('0101010101'):
        print('i = %s and pattern = %s' % (i, signal))
        break
else:
    print('found nothing')
















