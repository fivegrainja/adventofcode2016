#!/bin/python3

import collections

ELF_COUNT = 3004953

def solve_parttwo():
    left = collections.deque()
    right = collections.deque()
    for i in range(1, ELF_COUNT+1):
        if i < (ELF_COUNT // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] #or right[0]

print(solve_parttwo())