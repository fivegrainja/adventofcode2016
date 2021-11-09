#! /usr/local/bin/python3

import argparse
import string
import collections


def cmp_key(a):
    return (-1 * a[1], a[0])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='File of input data')
    args = parser.parse_args()

    input_file = open(args.input_file)
    input_lines = input_file.readlines()
    input_file.close()

    real_rooms = []

    for line in input_lines:
        x = line.find('[')
        a = line[:x]
        b = line[x:-1]
        parts = a.split('-')
        orig_name = ''.join(parts[:-1])
        name = orig_name.replace('-', '')
        sector = int(parts[-1])
        #print('input line: %s' % line.strip())
        #print('name: %s' % name)
        #print('sector: %s' % sector)
        c = collections.Counter(name)
        #print(c)

        common = sorted(c.most_common(), key=cmp_key, reverse=False)
        #print('sorted: %s' % common)
        top5 = ''.join([ltr for (ltr, cnt) in common[:5]])
        #print('top5: %s' % top5)
        checksum = b.strip('[]')
        #print('checksum: %s' % checksum)

        if checksum == top5:
            real_rooms.append((orig_name, sector))
        #print('')

    for (name, sector) in real_rooms:
        new_name = []
        for char in list(name):
            i = string.ascii_lowercase.find(char)
            ii = (i + sector) % 26
            new_name.append(string.ascii_lowercase[ii])
        new_name = ''.join(new_name)
        print('%s  sector: %s' % (new_name, sector))

