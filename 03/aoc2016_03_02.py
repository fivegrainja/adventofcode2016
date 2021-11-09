#! /usr/local/bin/python3

import argparse
import collections

num_triagles = 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='File of input data')
    args = parser.parse_args()

    input_file = open(args.input_file)
    input_lines = input_file.readlines()
    input_file.close()

    col_1 = []
    col_2 = []
    col_3 = []
    for line in input_lines:
        val_1, val_2, val_3 = [int(x) for x in line.split(' ') if x]
        col_1.append(val_1)
        col_2.append(val_2)
        col_3.append(val_3)
    values = collections.deque()
    values.extend(col_1)
    values.extend(col_2)
    values.extend(col_3)
    while values:
        a = values.popleft()
        b = values.popleft()
        c = values.popleft()
        print('%s %s %s' % (a, b, c))
        if a +  b > c and a + c > b and b + c > a:
            num_triagles += 1

print('Number of triangles is %s' % num_triagles)
