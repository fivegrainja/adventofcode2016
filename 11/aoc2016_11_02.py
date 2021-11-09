#! /usr/local/bin/python3

import argparse
import string
import collections
import hashlib
import copy
import cProfile
import heapq


# The first floor contains a promethium generator and a promethium-compatible microchip.
# The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
# The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
# The fourth floor contains nothing relevant.

# Test data
# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.

# 64 was too high for part B
# 60 was too high for part B
# 55 was too low for part B
# not 58, 56

test_data = True
do_profile = False
never_take_pair_down = True
no_double_down_if_singles = False
no_single_up_if_doubles = False
skip_empty_lower_levels = True

print('Configuration:')
print('test_data: %s' % test_data)

num_floors = 4

if test_data:
    # chips are positive, generators are negative
    hydrogen_chip, lithium_chip = tuple(range(1, 3))
    hydrogen_gen,  lithium_gen = tuple(range(-1, -3, -1))
    initial_state = (0, (
                        tuple(sorted([hydrogen_chip, lithium_chip])),
                        tuple(sorted([hydrogen_gen])),
                        tuple(sorted([lithium_gen]))
                        ))
else:
    promethium_chip, cobalt_chip, curium_chip, ruthenium_chip, plutonium_chip = range(1, 6)
    promethium_gen,  cobalt_gen,  curium_gen,  ruthenium_gen,  plutonium_gen = range(-1, -6, -1)
    initial_state = (0, (
                        tuple(sorted([promethium_gen, promethium_chip])),
                        tuple(sorted([cobalt_gen, curium_gen, ruthenium_gen, plutonium_gen])),
                        tuple(sorted([cobalt_chip, curium_chip, ruthenium_chip, plutonium_chip])),
                        tuple()
                        ))


def are_we_done(state):
    if state[1][0] or state[1][1] or state[1][2]
        return False
    return True


def is_state_tenable(state):
    for floor in state[1]:
        has_gen = floor and floor[0] < 0
        if has_gen:
            if [i in floor if i > 0 and -i not in floor]:
                return False
    return True


def get_potential_movers(state):
    current = state[0]
    potential_movers = itertools.combinations(state[1][current], 1)
    potential_movers += itertools.combinations(state[1][current], 2)
    return potential_movers


def is_empty_below_elevator(state):
    for floor in range(state[0]):
        if state[1][floor]:
            return False
    return True


def create_potential_move_up(state, movers):
    if state[0] == 3:
        return None
    base_state = copy.deepcopy(state)
    base_state[1][state[0]]



    global num_fingerprint_collisions
    # print('considering moving %s up' % movers)
    if state['elevator'] == 3:
        return None
    potential_state = {
        'elevator': state['elevator'],
        'floors': [
            set([i for i in state['floors'][0]]),
            set([i for i in state['floors'][1]]),
            set([i for i in state['floors'][2]]),
            set([i for i in state['floors'][3]]),
        ]
    }
    potential_state['floors'][state['elevator']] -= movers
    potential_state['floors'][state['elevator']+1] |= movers
    potential_state['elevator'] += 1
    fingerprint = get_fingerprint(potential_state)
    if fingerprint in previous_fingerprints:
        num_fingerprint_collisions += 1
    else:
        previous_fingerprints.add(fingerprint)
        if is_state_tenable(potential_state):
            return potential_state
    return None


def create_potential_move_down(state, movers):
    global num_fingerprint_collisions
    if state['elevator'] == 0:
        return None
    if never_take_pair_down and len(movers) == 2:
        movers_list = list(movers)
        if movers_list[0].split()[0] == movers_list[1].split()[0]:
            return None
    if skip_empty_lower_levels and is_empty_below_elevator(state):
        return None
    potential_state = {
        'elevator': state['elevator'],
        'floors':[
            set([i for i in state['floors'][0]]),
            set([i for i in state['floors'][1]]),
            set([i for i in state['floors'][2]]),
            set([i for i in state['floors'][3]]),
        ]
    }
    potential_state['floors'][state['elevator']] -= movers
    potential_state['floors'][state['elevator']-1] |= movers
    potential_state['elevator'] -= 1
    fingerprint = get_fingerprint(potential_state)
    if fingerprint in previous_fingerprints:
        num_fingerprint_collisions += 1
    else:
        previous_fingerprints.add(fingerprint)
        if is_state_tenable(potential_state):
            return potential_state
    return None


def possible_next_states(state):
    next_states = []
    potential_movers = get_potential_movers(state)
    # Moves up
    if state[0] < 3:
        for movers in potential_movers:
            next_state = copy.deepcopy(state)
            next_state[1][state[0]]

            next_states.append(
                (state[0]+1, (
                    tuple(sorted)
                    )

                    )
                )



def possible_next_states(state):
    next_states = []
    potential_movers = get_potential_movers(state)
    potential_single_movers = [m for m in potential_movers if len(m) == 1]
    potential_double_movers = [m for m in potential_movers if len(m) == 2]
    found_double_up = False
    for movers in potential_double_movers:
        potential_state = create_potential_move_up(state, movers)
        if potential_state:
            next_states.append(potential_state)
            found_double_up = True
    if not found_double_up or no_single_up_if_doubles:
        for mover in potential_single_movers:
            potential_state = create_potential_move_up(state, mover)
            if potential_state:
                next_states.append(potential_state)
    found_single_down = False
    for movers in potential_single_movers:
        potential_state = create_potential_move_down(state, movers)
        if potential_state:
            next_states.append(potential_state)
            found_single_down = True
    if not found_single_down or not no_double_down_if_singles:
        for mover in potential_double_movers:
            potential_state = create_potential_move_down(state, mover)
            if potential_state:
                next_states.append(potential_state)
    return next_states


def process_level(states, steps):
    global num_fingerprint_collisions
    global stop_after
    if stop_after > 0 and steps >= stop_after:
        print('stopping')
        return steps
    if not states:
        return 0
    print('Processing level %s: ' % steps)
    print('  states: %s' % len(states))
    print('  fingerprint collisions: %s' % num_fingerprint_collisions)
    print('  total states tested so far: %s' % num_states_tested)
    for state in states:
        if are_we_done(state):
            return steps
    next_states = []
    for state in states:
        next_states.extend(possible_next_states(state))
    if not next_states:
        print('next_states is empty')
    return process_level(next_states, steps+1)


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(state):
    # return small numbers the closer we are to goal
    # Distance of each from goal maybe
    floors = state['floors']
    return len(floors[0]) * 3 + len(floors[1]) * 2 + len(floors[2])


def a_star_search(start):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if are_we_done(current):
            break
        
        for next in possible_next_states(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next)
                #priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far


def go():
    global initial_state
    came_from, cost_so_far = a_star_search(initial_state)


if do_profile:
    cProfile.run('go()')
else:
    go()












