""" Day 9: Explosives in Cyberspace

Author: Ic4r0 - https://github.com/Ic4r0

Created: 3rd July 2022
"""

# Imports
from utils.parse_input import parse_single_line
from re import match


# Solutions
def part_1(file: str) -> int:
    """ Code for the 1st part of the 9th day of Advent of Code

    :param file: input string
    :return: numeric result
    """
    idx = 0
    uncompressed = ''
    while idx < len(file):
        if file[idx] != '(':
            uncompressed += file[idx]
            idx += 1
        else:
            close_idx = file.index(')', idx)
            match_marker = match(r'(\d+)x(\d+)', file[idx+1: close_idx])
            length, repetitions = match_marker.groups()
            uncompressed += file[close_idx+1:close_idx+int(length)+1] * int(repetitions)
            idx = close_idx + int(length) + 1
    return len(uncompressed)


def part_2(file: str) -> int:
    """ Code for the 2nd part of the 9th day of Advent of Code
    Idea from
    https://www.reddit.com/r/adventofcode/comments/5hbygy/comment/dazentu/?utm_source=share&utm_medium=web2x&context=3

    :param file: input string
    :return: numeric result
    """
    uncompressed_length = 0
    weigths_list = [1 for __ in range(len(file))]
    idx = 0
    while idx < len(file):
        if file[idx] != '(':
            uncompressed_length += weigths_list[idx]
            idx += 1
        else:
            close_idx = file.index(')', idx)
            match_marker = match(r'(\d+)x(\d+)', file[idx+1: close_idx])
            length, repetitions = match_marker.groups()
            for marker_length in range(close_idx+1, close_idx+int(length)+1):
                weigths_list[marker_length] = weigths_list[marker_length] * int(repetitions)
            idx = close_idx + 1
    return uncompressed_length


def day_9(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 9th day we want to execute

    :param selected_part: selected Advent of Code part of the 9th day
    :param test: flag to use test input
    """
    file = parse_single_line(9, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(file)
        print('The result of 1st part of the 9th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(file)
        print('The result of 2nd part of the 9th day of AoC is: ' + str(result_part_2))
