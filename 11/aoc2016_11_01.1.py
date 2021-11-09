#! /usr/local/bin/python3

import argparse
import string
import collections
import hashlib
import copy
import cProfile


# The first floor contains a promethium generator and a promethium-compatible microchip.
# The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
# The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
# The fourth floor contains nothing relevant.

previous_fingerprints = set()
num_fingerprint_collisions = 0




num_states_tested = 0   

# Test data
# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.

# 64 was too high for part B
# 60 was too high for part B
# 55 was too low for part B
# not 58, 56

test_data = False
part_b_data_only = False
stop_after = 60  # We know this is an upper bound from incorrect guess feedback
do_profile = False
never_take_pair_down = True
no_double_down_if_singles = True
no_single_up_if_doubles = True
skip_empty_lower_levels = True

print('Configuration:')
print('test_data: %s' % test_data)
print('stop_after: %s' % stop_after)


num_floors = 4
if test_data:
    initial_state = {
        'elevator': 0,
        'floors': [
            set(['hydrogen chip', 'lithium chip']),
            set(['hydrogen generator']),
            set(['lithium generator']),
            set()
            ]
    }
elif part_b_data_only:
    initial_state = {
        'elevator': 0,
        'floors': [
            set(['dilithium generator', 'dilithium chip',
                'elerium generator', 'elerium chip']),
            set(),
            set(),
            set()
            ]
    }
else:
    initial_state = {
        'elevator': 0,
        'floors': [
            set(['promethium generator', 'promethium chip',
                'dilithium generator', 'dilithium chip',
                'elerium generator', 'elerium chip']),
            set(['cobalt generator', 'curium generator', 'ruthenium generator',
                'plutonium generator']),
            set(['cobalt chip', 'curium chip', 'ruthenium chip', 'plutonium chip']),
            set()
            ]
    }


def are_we_done(state):
    global num_states_tested
    num_states_tested += 1
    for floor in range(3):
        if state['floors'][floor]:
            return False
    return True


def get_fingerprint(state):
    # elv = state['elevator']
    # return 'e%s-f0:%s-f1:%s-f2:%s-f3:%s' % (
    #     elv,
    #     ','.join(list(state['floors'][0])),
    #     ','.join(list(state['floors'][1])),
    #     ','.join(list(state['floors'][2])),
    #     ','.join(list(state['floors'][3])))
    disposition = collections.defaultdict(dict)  # [chip, generator]
    for floor_num in range(num_floors):
        for occupant in state['floors'][floor_num]:
            element, thing = occupant.split()
            disposition[element][thing] = floor_num
    fingerprint = [(v['chip'], v['generator']) for v in disposition.values()]
    fingerprint = '%s%s' % (state['elevator'], str(tuple(fingerprint)))
    return tuple(fingerprint)


def is_state_tenable(state):
    for floor_num in range(4):
        floor = state['floors'][floor_num]
        chip_elements = [i.split()[0] for i in floor if i.endswith('chip')]
        generator_elements = [i.split()[0] for i in floor if i.endswith('generator')]
        for e in chip_elements:
            if e not in generator_elements and generator_elements:
                return False
    return True


def get_potential_movers(state):
    potential_movers = []
    for i in state['floors'][state['elevator']]:
        potential_movers.append(set([i]))
        for j in state['floors'][state['elevator']]:
            if i != j:
                if set([i, j]) not in potential_movers:
                    potential_movers.append(set([i, j]))
    return potential_movers


def is_empty_below_elevator(state):
    for f in range(state['elevator']):
        if state['floors'][f]:
            return False
    return True


def create_potential_move_up(state, movers):
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

def go():
    global initial_state
    min_steps = process_level([initial_state], 0)
    print('min steps: %s' % min_steps)

if do_profile:
    cProfile.run('go()')
else:
    go()












