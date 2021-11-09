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
        #parts = line.split('[]')
        parts = line.replace('[', ' ').replace(']', ' ').split()
        if line[0] == '[':
            inside = True
        else:
            inside = False

        foundAbba = False
        print('parts an %s' % parts)
        #print('starting with inside=%s' % inside)
        for part in parts:
            print('%s is inside=%s' % (part, inside))
            for i in range(len(part) - 3):
                if part[i] != part[i+1] and part[i] == part[i+3] and part[i+1] == part[i+2]:
                    if inside:
                        print('found abba inside')
                        return False
                    else:
                        print('found abba outside')
                        foundAbba = True
                        break
            inside =  not inside
        return foundAbba


    num_supported = 0
    for l in input_lines:
        if check_line(l):
            print ('yes: %s' % l)
            num_supported += 1
        else:
            print('no: %s' % l)

    print('num supportid: %s' % num_supported)

