""" Day 2: Bathroom Security

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd July 2022
"""

# Imports
from utils.parse_input import parse_by_line


# Solutions
def part_1(input_list: list) -> str:
    """ Code for the 1st part of the 2nd day of Advent of Code

    :param input_list: input list
    :return: string result
    """
    current_button = 5
    password_sequence = ''
    for password_digit in input_list:
        for instruction in password_digit:
            match instruction:
                case 'L':
                    if current_button % 3 != 1:
                        current_button -= 1
                case 'U':
                    if current_button > 3:
                        current_button -= 3
                case 'R':
                    if current_button % 3 != 0:
                        current_button += 1
                case 'D':
                    if current_button < 7:
                        current_button += 3
        password_sequence += str(current_button)
    return password_sequence


def part_2(input_list: list) -> str:
    """ Code for the 2nd part of the 2nd day of Advent of Code

    :param input_list: input list
    :return: string result
    """
    current_button = 5
    password_sequence = ''
    replace_value = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D'
    }
    for password_digit in input_list:
        for instruction in password_digit:
            match instruction:
                case 'L':
                    if current_button not in [1, 2, 5, 10, 13]:
                        current_button -= 1
                case 'U':
                    if current_button not in [1, 2, 4, 5, 9] and current_button in [3, 13]:
                        current_button -= 2
                    elif current_button not in [1, 2, 4, 5, 9]:
                        current_button -= 4
                case 'R':
                    if current_button not in [1, 4, 9, 12, 13]:
                        current_button += 1
                case 'D':
                    if current_button not in [5, 9, 10, 12, 13] and current_button in [1, 11]:
                        current_button += 2
                    elif current_button not in [5, 9, 10, 12, 13]:
                        current_button += 4
        password_sequence += replace_value.get(current_button, str(current_button))
    return password_sequence


def day_2(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 2nd day we want to execute

    :param selected_part: selected Advent of Code part of the 2nd day
    :param test: flag to use test input
    """
    instructions = [list(line) for line in parse_by_line(2, False, is_test=test)]
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(instructions)
        print('The result of 1st part of the 2nd day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(instructions)
        print('The result of 2nd part of the 2nd day of AoC is: ' + str(result_part_2))
