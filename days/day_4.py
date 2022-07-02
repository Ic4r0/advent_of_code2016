""" Day 4: Security Through Obscurity

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd July 2022
"""

# Imports
from utils.parse_input import parse_by_line
from collections import Counter


# Utils
def split_room_parts(room: str) -> tuple[list, list, int, str]:
    """ Util to split room in the different parts: encrypted name, sector ID and checksum

    :param room: string to parse
    :return: tuple containing the splitted parts
    """
    square_bracket_idx = room.index('[')
    checksum = room[square_bracket_idx + 1: -1]
    name_and_id = room[: square_bracket_idx].split('-')
    encrypted_name = name_and_id[:-1]
    encrypted_name_joined = ''.join(encrypted_name)
    chars_counter = Counter(encrypted_name_joined)
    chars_counter_ordered_list = sorted(
        [(char, chars_counter[char]) for char in chars_counter],
        key=lambda x: (-x[1], x[0])
    )
    sector_id = int(name_and_id[-1])
    return encrypted_name, chars_counter_ordered_list, sector_id, checksum


def check_room_validity(occurrences: list, checksum: str) -> bool:
    """ Util to check room validity

    :param occurrences: chars occurrences ordered list
    :param checksum: room checksum
    :return: valid room
    """
    computed_checksum = ''.join(char for char, __ in occurrences)
    if len(computed_checksum) > 5:
        computed_checksum = computed_checksum[:5]
    return computed_checksum == checksum


def shift_cipher(string: str, shifts: int) -> str:
    """ Util to check room validity

    :param string: string to encipher
    :param shifts: number of char shifts
    :return: new string
    """
    return ''.join([chr((ord(char) + shifts - 97) % 26 + 97) for char in string])


# Solutions
def part_1(input_list: list[tuple[list, list, int, str]]) -> int:
    """ Code for the 1st part of the 4th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    id_sum = 0
    for __, occurrences, sector_id, checksum in input_list:
        if check_room_validity(occurrences, checksum):
            id_sum += sector_id
    return id_sum


def part_2(input_list: list[tuple[list, list, int, str]]) -> int:
    """ Code for the 2nd part of the 4th day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    valid_rooms = []
    for splitted_name, occurrences, sector_id, checksum in input_list:
        if check_room_validity(occurrences, checksum):
            valid_rooms.append(([shift_cipher(string, sector_id) for string in splitted_name], sector_id))
    __, sector_id = [(name, s_id) for name, s_id in valid_rooms if any([part == 'northpole' for part in name])][0]
    return sector_id


def day_4(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 4th day we want to execute

    :param selected_part: selected Advent of Code part of the 4th day
    :param test: flag to use test input
    """
    rooms = [split_room_parts(line) for line in parse_by_line(4, False, is_test=test)]
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(rooms)
        print('The result of 1st part of the 4th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(rooms)
        print('The result of 2nd part of the 4th day of AoC is: ' + str(result_part_2))
