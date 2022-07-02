""" Day 3: Squares With Three Sides

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd July 2022
"""

# Imports
from utils.parse_input import parse_by_line


# Solutions
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 3rd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    valid_triangles = 0
    for a, b, c in input_list:
        if a < b + c and b < a + c and c < a + b:
            valid_triangles += 1
    return valid_triangles


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 3rd day of Advent of Code

    :param input_list: input list
    :return: numeric result
    """
    valid_triangles = 0
    supp_list = input_list[:]
    while supp_list:
        triangles = [[], [], []]
        for idx in range(3):
            side_0, side_1, side_2 = supp_list.pop()
            triangles[0].append(side_0)
            triangles[1].append(side_1)
            triangles[2].append(side_2)
        for a, b, c in triangles:
            if a < b + c and b < a + c and c < a + b:
                valid_triangles += 1
    return valid_triangles


def day_3(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 3rd day we want to execute

    :param selected_part: selected Advent of Code part of the 3rd day
    :param test: flag to use test input
    """
    triangle_sides = [[int(value) for value in line.split()] for line in parse_by_line(3, False, is_test=test)]
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(triangle_sides)
        print('The result of 1st part of the 3rd day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(triangle_sides)
        print('The result of 2nd part of the 3rd day of AoC is: ' + str(result_part_2))
