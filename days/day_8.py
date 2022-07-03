""" Day 8: Two-Factor Authentication

Author: Ic4r0 - https://github.com/Ic4r0

Created: 3rd July 2022
"""

# Imports
from utils.parse_input import parse_by_line
from re import match
from collections import deque


# Utils
def command_rect(screen: list, width: int, height: int) -> list:
    """ Util to use command RECT

    :param screen: screen current state
    :param width: rect width
    :param height: rect height
    :return: new list
    """
    return [
        ['#' if x < width and y < height else screen[y][x] for x in range(len(screen[0]))]
        for y in range(len(screen))
    ]


def command_rotate_column(screen: list, column: int, shift: int) -> list:
    """ Util to use command ROTATE COLUMN

    :param screen: screen current state
    :param column: selected column
    :param shift: shift
    :return: new list
    """
    column_values = [row[column] for row in screen]
    deque_column = deque(column_values)
    deque_column.rotate(shift)
    shifted_column_values = list(deque_column)
    for idx in range(len(shifted_column_values)):
        screen[idx][column] = shifted_column_values[idx]
    return screen


def command_rotate_row(screen: list, row: int, shift: int) -> list:
    """ Util to use command ROTATE ROW

    :param screen: screen current state
    :param row: selected row
    :param shift: shift
    :return: new list
    """
    row_values = screen[row]
    deque_row = deque(row_values)
    deque_row.rotate(shift)
    shifted_row_values = list(deque_row)
    for idx in range(len(shifted_row_values)):
        screen[row][idx] = shifted_row_values[idx]
    return screen


def pretty_print_screen(screen: list) -> None:
    """ Util to pretty print the screen

    :param screen: screen current state
    :return: new list
    """
    for row in screen:
        print(''.join(row))
    print()


# Solutions
def part_1(screen_size: list, commands: list) -> int:
    """ Code for the 1st part of the 8th day of Advent of Code

    :param screen_size: screen
    :param commands: input list
    :return: numeric result
    """
    new_screen = screen_size[:]
    for command in commands:
        match command[0]:
            case 'rect':
                new_screen = command_rect(new_screen, command[1], command[2])
            case 'rotate column':
                new_screen = command_rotate_column(new_screen, command[1], command[2])
            case 'rotate row':
                new_screen = command_rotate_row(new_screen, command[1], command[2])
    return sum(sum(1 if pixel == '#' else 0 for pixel in row) for row in new_screen)


def part_2(screen_size: list, commands: list) -> list:
    """ Code for the 2nd part of the 8th day of Advent of Code

    :param screen_size: screen
    :param commands: input list
    :return: screen current state
    """
    new_screen = screen_size[:]
    for command in commands:
        match command[0]:
            case 'rect':
                new_screen = command_rect(new_screen, command[1], command[2])
            case 'rotate column':
                new_screen = command_rotate_column(new_screen, command[1], command[2])
            case 'rotate row':
                new_screen = command_rotate_row(new_screen, command[1], command[2])
    return new_screen


def day_8(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 8th day we want to execute

    :param selected_part: selected Advent of Code part of the 8th day
    :param test: flag to use test input
    """
    parsed_file = parse_by_line(8, False, is_test=test)
    commands = []
    for line in parsed_file:
        match_rect = match(r'rect (\d+)x(\d+)', line)
        match_rot_col = match(r'rotate column x=(\d+) by (\d+)', line)
        match_rot_row = match(r'rotate row y=(\d+) by (\d+)', line)
        if match_rect:
            width, height = match_rect.groups()
            commands.append(('rect', int(width), int(height)))
        elif match_rot_col:
            column, shift = match_rot_col.groups()
            commands.append(('rotate column', int(column), int(shift)))
        elif match_rot_row:
            row, shift = match_rot_row.groups()
            commands.append(('rotate row', int(row), int(shift)))
    max_width = 50 if not test else 7
    max_height = 6 if not test else 3
    screen_size = [['.' for _ in range(max_width)] for _ in range(max_height)]
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(screen_size, commands)
        print('The result of 1st part of the 8th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(screen_size, commands)
        print('The result of 2nd part of the 8th day of AoC is: \n')
        pretty_print_screen(result_part_2)
