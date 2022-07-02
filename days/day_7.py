""" Day 7: Internet Protocol Version 7

Author: Ic4r0 - https://github.com/Ic4r0

Created: 2nd July 2022
"""

# Imports
from utils.parse_input import parse_by_line


# Utils
def check_abba(ip: str) -> bool:
    """ Util to check if IP part is ABBA

    :param ip: IP part to check for ABBA
    :return: is ABBA
    """
    if len(ip) < 4:
        return False
    for idx in range(len(ip) - 3):
        if ip[idx] != ip[idx+1] and f'{ip[idx:idx+2]}' == f'{ip[idx+3]}{ip[idx+2]}':
            return True
    return False


def get_bab_from_aba(supernet_sequences: list) -> list:
    """ Util to get possible BAB from supernet sequences of an IP

    :param supernet_sequences: supernet sequences of an IP
    :return: list of possible BAB
    """
    possible_bab = []
    for supernet in supernet_sequences:
        if len(supernet) < 3:
            continue
        for idx in range(len(supernet) - 2):
            if supernet[idx] != supernet[idx+1] and supernet[idx] == supernet[idx+2]:
                possible_bab.append(f'{supernet[idx+1]}{supernet[idx]}{supernet[idx+1]}')
    return possible_bab


def differentiate_ip_parts(ip: str) -> tuple:
    """ Util to split IP in different type of parts

    :param ip: IP to be split in different type of parts
    :return: separated IP parts
    """
    supernet = []
    hypernet = []
    if '[' in ip:
        idx_open_bracket = ip.index('[')
        idx_close_bracket = ip.index(']')
        supernet.append(ip[:idx_open_bracket])
        hypernet.append(ip[idx_open_bracket+1: idx_close_bracket])
        sup, hyp = differentiate_ip_parts(ip[idx_close_bracket+1:])
        supernet.extend(sup)
        hypernet.extend(hyp)
    else:
        supernet = [ip]
    return supernet, hypernet


# Solutions
def part_1(ip_list: list) -> int:
    """ Code for the 1st part of the 7th day of Advent of Code

    :param ip_list: input list
    :return: numeric result
    """
    valid_ip = 0
    for ip in ip_list:
        sup, hyp = differentiate_ip_parts(ip)
        if any([check_abba(single_sup) for single_sup in sup]) \
                and all([not check_abba(single_hyp) for single_hyp in hyp]):
            valid_ip += 1
    return valid_ip


def part_2(ip_list: list) -> int:
    """ Code for the 2nd part of the 7th day of Advent of Code

    :param ip_list: input list
    :return: numeric result
    """
    valid_ip = 0
    for ip in ip_list:
        sup, hyp = differentiate_ip_parts(ip)
        possible_bab = get_bab_from_aba(sup)
        for bab in possible_bab:
            if any([bab in single_hyp for single_hyp in hyp]):
                valid_ip += 1
                break
    return valid_ip


def day_7(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 7th day we want to execute

    :param selected_part: selected Advent of Code part of the 7th day
    :param test: flag to use test input
    """
    ip_list = parse_by_line(7, False, is_test=test)
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(ip_list)
        print('The result of 1st part of the 7th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(ip_list)
        print('The result of 2nd part of the 7th day of AoC is: ' + str(result_part_2))
