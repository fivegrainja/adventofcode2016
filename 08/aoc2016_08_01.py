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

    num_rows = 6
    num_cols = 50

    pix = []
    for r in range(num_rows):
        pix.append([])
        for c in range(num_cols):
            pix[r].append(0)


    def do_rect(row, col):
        for r in range(row):
            for c in range(col):
                pix[r][c] = 1

    def do_rotate_row(row, num):
        the_row = pix[row]
        for i in range(num):
            v = the_row.pop()
            the_row.insert(0, v)

    def do_rotate_col(col, num):
        print('rotate col col=%s num=%s' % (col,num))
        rng = list(range(1, num_rows))
        rng.reverse()
        for n in range(num):
            bottom =  pix[num_rows-1][col]
            for i in rng:
                pix[i][col] = pix[i-1][col]
            pix[0][col] = bottom

    answer = 0
    for l in input_lines:
        parts = l.split()
        print('parts is %s' % parts)
        command = parts[0]
        if command == 'rect':
            col, row = parts[1].split('x')
            do_rect(int(row), int(col))
        elif command == 'rotate' and parts[1] == 'row':
            row = parts[2].split('=')[-1]
            num = parts[4]
            do_rotate_row(int(row), int(num))
        elif command == 'rotate' and parts[1] == 'column':
            col = parts[2].split('=')[-1]
            num = parts[4]
            do_rotate_col(int(col), int(num))
        else:
            raise Exception('Bad command %s' % command)
        print('line= %s' % l)
        for i in range(num_rows):
            print(pix[i])
        print()

    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            count += pix[r][c]

    print('count is %s' % count)







