#! /usr/local/bin/python3

import argparse
import string
import collections
import hashlib


if __name__ == '__main__':

    door_id = 'cxdnnyjw'
    #door_id = 'abc'
    passcode = []

    i = 0
    while len(passcode) < 8:
        m = hashlib.md5()
        b = bytearray(door_id + str(i), 'utf-8')
        m.update(b)
        digest = m.hexdigest()
        #print('%s' % digest)
        if digest[:5] == '00000':
            passcode.append(digest[5])
            print('passcode = %s' % ''.join(passcode))
        i += 1

    print('passcode is %s' % ''.join(passcode))




