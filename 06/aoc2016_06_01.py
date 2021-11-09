#! /usr/local/bin/python3

import argparse
import string
import collections

LENGTH = 8

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='File of input data')
    args = parser.parse_args()

    input_file = open(args.input_file)
    input_lines = input_file.readlines()
    input_file.close()

    counters = []
    for i in range(LENGTH):
        counters.append(collections.Counter())

    for line in input_lines:
        for i in range(LENGTH):
            counters[i][line[i]] += 1

    print('most common:')
    code = []
    for i in range(LENGTH):
        code.append(counters[i].most_common(1)[0][0])
    print(''.join(code))
    
  