#! /usr/local/bin/python3

import argparse

keypad = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

x = 1
y = 1

def move(direction):
    global x
    global y
    if direction == 'U':
        if y > 0:
            y -= 1
    elif direction == 'D':
        if y < 2:
            y += 1
    elif direction == 'L':
        if x > 0:
            x -= 1
    elif direction == 'R':
        if x < 2:
            x += 1
    else:
        raise Exception('Bad direction: %s' % direction)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='File of input data')
    args = parser.parse_args()

    input_file = open(args.input_file)
    input_lines = input_file.readlines()
    input_file.close()

    combination = []
    for line in input_lines:
        for direction in list(line.strip()):
            move(direction)
        combination.append(keypad[y][x])

    print('Combination is %s' % combination)
