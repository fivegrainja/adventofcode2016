#! /usr/local/bin/python3

import argparse
import string
import collections
import hashlib


if __name__ == '__main__':

    door_id = 'cxdnnyjw'
    #door_id = 'abc'
    passcode = 8 * [None]

    i = 0
    count = 0
    while count < 8:
        m = hashlib.md5()
        b = bytearray(door_id + str(i), 'utf-8')
        m.update(b)
        digest = m.hexdigest()
        if digest[:5] == '00000':
            position = digest[5]
            if position in string.digits:
                position = int(position)
                if position >=0 and position < 8 and passcode[position] == None:
                    passcode[position] = digest[6]
                    count += 1
                    print('count is %s' % count)
                    #print('passcode = %s' % ''.join(passcode))
        i += 1

    print('passcode is %s' % ''.join(passcode))




