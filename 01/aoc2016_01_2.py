#! /usr/local/bin/python3

import argparse
import collections

class BunnyHunter:

    def __init__(self):
        self.compass = collections.deque(['N', 'E', 'S', 'W'])
        self.east = 0
        self.north = 0
        self.history = set()

    def turn(self, direction):
        if direction == 'R':
            self.compass.rotate(-1)
        elif direction == 'L':
            self.compass.rotate(1)
        else:
            raise('Bad direction: %s' % direction)

    def deja_vu(self):
        return (self.east, self.north) in self.history

    def remember(self):
        self.history.add((self.east, self.north))

    def proceed(self, distance):
        for steps in range(1, distance+1):
            if self.compass[0] == 'N':
                self.north += 1
            elif self.compass[0] == 'S':
                self.north -= 1
            elif self.compass[0] == 'E':
                self.east += 1
            else:
                self.east -= 1
            if self.deja_vu():
                return True
            self.remember()
        return False

    def follow_instructions(self, instructions):
        for i in instructions:
            direction = i[0]
            distance = int(i[1:])
            self.turn(direction)
            done = self.proceed(distance)
            if done:
                break

    def get_distance_from_start(self):
        return abs(self.east) + abs(self.north)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='File of input data')
    args = parser.parse_args()

    input_file = open(args.input_file)
    input = input_file.read()
    input_file.close()
    instructions = [c.strip() for c in input.split(',')]

    santas_minion = BunnyHunter()
    santas_minion.follow_instructions(instructions)
    distance = santas_minion.get_distance_from_start()

    print('Blocks from origin: %s' % distance)
