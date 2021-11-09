#! /usr/local/bin/python3

import argparse
import string
import collections
import hashlib
import sys
from pprint import pprint

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
    input_lines = list(input_file.readlines())
    input_file.close()

    holdings = collections.defaultdict(list)
    behaviors = collections.defaultdict(list)

    def give(giver, receiver, chip):
        if giver:
            holdings[giver].remove(chip)
        holdings[receiver].append(chip)
        if receiver.startswith('bot') and len(holdings[receiver]) == 2:
            val1, val2 = holdings[receiver]
            lower_val = min(val1, val2)
            higher_val = max(val1, val2)
            if lower_val == 17 and higher_val == 61:
                for k in holdings.keys():
                    if k.startswith('output'):
                        print('%s is %s' % (k, holdings[k]))
                # print('holdings = %s' %)
                print('%s compared 17 and 61' % receiver)
                # sys.exit(1)
            # print('receiver is %s' % receiver)
            # print('receiver behaviors are %s' % behaviors[receiver])
            # print()
            # print()
            # pprint('behaviors are %s' % behaviors)
            # print()
            # print()
            give(receiver, behaviors[receiver][0], lower_val)
            give(receiver, behaviors[receiver][1], higher_val)

    for line in input_lines:
        line = line.strip()
        parts = line.split()
        if parts[0] == 'value':
            # holdings[parts[5]].append(int(parts[1]))
            pass
        elif parts[0] == 'bot':
            behaviors[' '.join([parts[0], parts[1]])] = [
                                        ' '.join([parts[5], parts[6]]),
                                        ' '.join([parts[10], parts[11]])]
        else:
            raise Exception('Do not understand line %s' % line)

    for line in input_lines:
        line = line.strip()
        parts = line.split()
        if parts[0] == 'value':
            give(None, ' '.join([parts[4], parts[5]]), int(parts[1]))


    print('output 0 is %s' % holdings['output 0'])
    print('output 1 is %s' % holdings['output 1'])
    print('output 2 is %s' % holdings['output 2'])
