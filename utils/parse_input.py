""" Util to parse Advent of Code inputs

Author: Ic4r0 - https://github.com/Ic4r0

Created: 1st December 2021
"""
import os


def parse_by_line(selected_day: int, int_list: bool = True, is_test: bool = False) -> list:
    """ Parse input file from a selected day by line

    :param selected_day: selected Advent of Code day
    :param int_list: flag to indicate which type each element of the returned list has to have. int if True,
        str otherwise
    :param is_test: flag to parse a test input
    :return: list containing file parsed by line
    """
    file_path = os.getcwd() + '\\inputs\\input_' + str(selected_day).zfill(2)
    if is_test:
        file_path += '_test'
    if os.path.isfile(file_path):
        with open(file_path) as file:
            if int_list:
                list_from_file = [int(line) for line in file.readlines()]
            else:
                list_from_file = [line.rstrip() for line in file.readlines()]
        return list_from_file
    else:
        raise IOError('There is no input file for day ' + str(selected_day))


def parse_single_line(selected_day: int, is_test: bool = False) -> str:
    """ Parse input file from a selected day as a single line

    :param selected_day: selected Advent of Code day
    :param is_test: flag to parse a test input
    :return: string containing file parsed by single line
    """
    file_path = os.getcwd() + '\\inputs\\input_' + str(selected_day).zfill(2)
    if is_test:
        file_path += '_test'
    if os.path.isfile(file_path):
        with open(file_path) as file:
            single_line = file.read()
        return single_line.rstrip()
    else:
        raise IOError('There is no input file for day ' + str(selected_day))
