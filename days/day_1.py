""" Day 1: No Time for a Taxicab

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd July 2022
"""

# Imports
from utils.parse_input import parse_single_line


# Utils methods
def compute_min_steps(input_list: list, stop_on_visit_twice: bool = False) -> int:
    """ Util function to compute the minimum distance between starting point and destination

    :param input_list: input list
    :param stop_on_visit_twice: flag for stopping on the first location you visit twice
    :return: numeric result
    """
    position = (0, 0)
    current_direction = 'N'
    visited_positions = [position]
    stop_iteration = False
    for turn, steps in input_list:
        if stop_iteration:
            break
        unit_x, unit_y = (0, 0)
        if (current_direction == 'N' and turn == 'R') or (current_direction == 'S' and turn == 'L'):
            current_direction = 'E'
            unit_x, unit_y = (1, 0)
        elif (current_direction == 'E' and turn == 'R') or (current_direction == 'W' and turn == 'L'):
            current_direction = 'S'
            unit_x, unit_y = (0, -1)
        elif (current_direction == 'S' and turn == 'R') or (current_direction == 'N' and turn == 'L'):
            current_direction = 'W'
            unit_x, unit_y = (-1, 0)
        elif (current_direction == 'W' and turn == 'R') or (current_direction == 'E' and turn == 'L'):
            current_direction = 'N'
            unit_x, unit_y = (0, 1)
        for __ in range(steps):
            position = (position[0] + unit_x, position[1] + unit_y)
            if stop_on_visit_twice and position in visited_positions:
                stop_iteration = True
                break
            elif stop_on_visit_twice:
                visited_positions.append(position)
    return abs(position[0]) + abs(position[1])


# Solutions
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 1st day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    return compute_min_steps(input_list)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 1st day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    return compute_min_steps(input_list, True)


def day_1(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 1st day we want to execute

    :param selected_part: selected Advent of Code part of the 1st day
    :param test: flag to use test input
    """
    directions = [(pair[0], int(pair[1:])) for pair in parse_single_line(1, is_test=test).split(', ')]
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(directions)
        print('The result of 1st part of the 1st day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(directions)
        print('The result of 2nd part of the 1st day of AoC is: ' + str(result_part_2))
