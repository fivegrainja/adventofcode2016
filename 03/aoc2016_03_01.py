#! /usr/local/bin/python3

import argparse

num_triagles = 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='File of input data')
    args = parser.parse_args()

    input_file = open(args.input_file)
    input_lines = input_file.readlines()
    input_file.close()

    for line in input_lines:
        a, b, c = [int(x) for x in line.split(' ') if x]
        print('%s %s %s' % (a, b, c))
        if a +  b > c and a + c > b and b + c > a:
            num_triagles += 1

print('Number of triangles is %s' % num_triagles)
