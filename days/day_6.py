""" Day 6: Signals and Noise

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd July 2022
"""

# Imports
from utils.parse_input import parse_by_line
from collections import Counter


# Solutions
def part_1(rep_message_signal: list) -> str:
    """ Code for the 1st part of the 6th day of Advent of Code

    :param rep_message_signal: input list
    :return: message
    """
    message = ''
    for idx in range(len(rep_message_signal[0])):
        occurrences = Counter(''.join([line[idx] for line in rep_message_signal]))
        chars_counter_ordered_list = sorted(
            [(char, occurrences[char]) for char in occurrences],
            key=lambda x: -x[1]
        )
        message += chars_counter_ordered_list[0][0]
    return message


def part_2(rep_message_signal: list) -> str:
    """ Code for the 2nd part of the 6th day of Advent of Code

    :param rep_message_signal: input list
    :return: password
    """
    message = ''
    for idx in range(len(rep_message_signal[0])):
        occurrences = Counter(''.join([line[idx] for line in rep_message_signal]))
        chars_counter_ordered_list = sorted(
            [(char, occurrences[char]) for char in occurrences],
            key=lambda x: x[1]
        )
        message += chars_counter_ordered_list[0][0]
    return message


def day_6(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 6th day we want to execute

    :param selected_part: selected Advent of Code part of the 6th day
    :param test: flag to use test input
    """
    rep_message_signal = parse_by_line(6, False, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(rep_message_signal)
        print('The result of 1st part of the 6th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(rep_message_signal)
        print('The result of 2nd part of the 6th day of AoC is: ' + str(result_part_2))
