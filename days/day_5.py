""" Day 5: How About a Nice Game of Chess?

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd July 2022
"""

# Imports
import string

from utils.parse_input import parse_single_line
import hashlib
from random import choice
import os


# Solutions
def part_1(door_id: str) -> str:
    """ Code for the 1st part of the 5th day of Advent of Code

    :param door_id: input string
    :return: password
    """
    int_idx = 0
    password = ''
    while len(password) < 8:
        md5_hash = hashlib.md5(f'{door_id}{int_idx}'.encode('utf-8')).hexdigest()
        if md5_hash[:5] == '00000':
            password += md5_hash[5]
        int_idx += 1
    return password


def part_2(door_id: str) -> str:
    """ Code for the 2nd part of the 5th day of Advent of Code

    :param door_id: input string
    :return: password
    """
    int_idx = 0
    password = '________'
    digits_found = 0
    while digits_found < 8:
        random_password = ''.join(choice('0123456789abcdef') for n in range(8))
        md5_hash = hashlib.md5(f'{door_id}{int_idx}'.encode('utf-8')).hexdigest()
        if md5_hash[:5] == '00000' and md5_hash[5] in string.hexdigits \
                and 0 <= int(md5_hash[5], 16) <= 7 and password[int(md5_hash[5], 16)] == '_':
            supp_list = list(password)
            supp_list[int(md5_hash[5], 16)] = md5_hash[6]
            password = ''.join(supp_list)
            digits_found += 1
        for idx in range(len(password)):
            if password[idx] != '_':
                supp_list = list(random_password)
                supp_list[idx] = password[idx]
                random_password = ''.join(supp_list)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(random_password)
        int_idx += 1
    return password


def day_5(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 5th day we want to execute

    :param selected_part: selected Advent of Code part of the 5th day
    :param test: flag to use test input
    """
    door_id = parse_single_line(5, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(door_id)
        print('The result of 1st part of the 5th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(door_id)
        print('The result of 2nd part of the 5th day of AoC is: ' + str(result_part_2))
