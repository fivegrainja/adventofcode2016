#! /usr/local/bin/python3

import argparse
import string
import collections

# new_list = sorted(old_list, key=key_providing_function, reverse=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='File of input data')
    args = parser.parse_args()

    input_file = open(args.input_file)
    input_lines = input_file.readlines()
    input_file.close()

    def check_line(line):
        parts = line.replace('[', ' ').replace(']', ' ').split()
        if line[0] == '[':
            inside = True
        else:
            inside = False

        aba = []
        bab = []

        for part in parts:
            for i in range(len(part) - 2):
                if part[i] != part[i+1] and part[i] == part[i+2]:
                    if inside:
                        bab.append(part[i:i+3])
                    else:
                        aba.append('%s%s%s' % (part[i+1], part[i], part[i+1]))
            inside = not inside
        print('line is %s' % line.strip())
        print('aba is %s' % aba)
        print('bab is %s' % bab)

        for x in aba:
            if x in bab:
                print('%s is in both\n' % x)
                return True
        print('returning false\n')
        return False

    num_supported = 0
    for l in input_lines:
        if check_line(l):
            num_supported += 1

    print('number supported %s' % num_supported)

