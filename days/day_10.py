""" Day 10: Balance Bots

Author: Ic4r0 - https://github.com/Ic4r0

Created: 3rd July 2022
"""

# Imports
from utils.parse_input import parse_by_line
from re import match


# Utils
def get_active_bot(bots_values: dict) -> int:
    """ Util to get the first bot that can act

    :param bots_values: dict containing starting values for each bot
    :return: numeric result
    """
    for bot, values in bots_values.items():
        if len(values) == 2:
            return bot


def check_compared_values(bots_values: dict, values_to_check: list) -> str:
    """ Util to check the compared values

    :param bots_values: dict containing starting values for each bot
    :param values_to_check: compare values
    :return: string result
    """
    for bot, values in bots_values.items():
        if len(values) == 2 and set(values) == set(values_to_check):
            return bot
    return 'None'


def check_outputs(bots_values: dict) -> int:
    """ Util to check if outputs 0, 1 and 2 are filled

    :param bots_values: dict containing starting values for each bot
    :return: numeric result
    """
    if bots_values.get('output0') and bots_values.get('output1') and bots_values.get('output2'):
        return int(bots_values['output0'][0]) * int(bots_values['output1'][0]) * int(bots_values['output2'][0])
    return 0


def set_bot_value(bots_values: dict, value_to_set: str, is_bot: bool, bot_number: str) -> None:
    """ Util to check the compared values

    :param bots_values: dict containing starting values for each bot
    :param value_to_set: value to set
    :param is_bot: is bot or output
    :param bot_number: bot or output number
    :return: None
    """
    bot_name = bot_number if is_bot else f'output{bot_number}'
    if not bots_values.get(bot_name):
        bots_values[bot_name] = []
    bots_values[bot_name].append(value_to_set)


# Solutions
def part_1(bots_values: dict, instructions: list, test: bool) -> int:
    """ Code for the 1st part of the 10th day of Advent of Code

    :param bots_values: dict containing starting values for each bot
    :param instructions: instructions for each bot
    :param test: is test
    :return: numeric result
    """
    values_to_check = ['2', '5'] if test else ['17', '61']
    bots = bots_values.copy()
    instr_copy = instructions[:]
    bot_with_wanted_values = -1
    while instr_copy:
        bot_with_wanted_values = check_compared_values(bots, values_to_check)
        if bot_with_wanted_values != 'None':
            break
        bot = get_active_bot(bots)
        __, low_is_bot, low_n, high_is_bot, high_n = [instr for instr in instr_copy if instr[0] == bot][0]
        bot_values = [int(value) for value in bots[bot]]
        low_value = str(min(bot_values))
        set_bot_value(bots, low_value, low_is_bot, low_n)
        high_value = str(max(bot_values))
        set_bot_value(bots, high_value, high_is_bot, high_n)
        bots[bot] = []
    return int(bot_with_wanted_values)


def part_2(bots_values: dict, instructions: list) -> int:
    """ Code for the 2nd part of the 10th day of Advent of Code

    :param bots_values: dict containing starting values for each bot
    :param instructions: instructions for each bot
    :return: numeric result
    """
    bots = bots_values.copy()
    instr_copy = instructions[:]
    output_products = 0
    while instr_copy:
        output_products = check_outputs(bots)
        if output_products:
            break
        bot = get_active_bot(bots)
        __, low_is_bot, low_n, high_is_bot, high_n = [instr for instr in instr_copy if instr[0] == bot][0]
        bot_values = [int(value) for value in bots[bot]]
        low_value = str(min(bot_values))
        set_bot_value(bots, low_value, low_is_bot, low_n)
        high_value = str(max(bot_values))
        set_bot_value(bots, high_value, high_is_bot, high_n)
        bots[bot] = []
    return output_products


def day_10(selected_part: int = None, test: bool = False):
    """ Needed to select which part of the 10th day we want to execute

    :param selected_part: selected Advent of Code part of the 10th day
    :param test: flag to use test input
    """
    instructions_from_files = parse_by_line(10, False, is_test=test)
    bots_values = {}
    instructions = []
    for line in instructions_from_files:
        match_value_to = match(r'value (\d+) goes to bot (\d+)', line)
        match_bot_gives = match(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', line)
        if match_value_to:
            value, bot = match_value_to.groups()
            if not bots_values.get(bot):
                bots_values[bot] = []
            bots_values[bot].append(value)
        elif match_bot_gives:
            bot_n, low_bot_or_output, low_n, high_bot_or_output, high_n = match_bot_gives.groups()
            instructions.append((
                bot_n,
                low_bot_or_output == 'bot',
                low_n,
                high_bot_or_output == 'bot',
                high_n
            ))
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(bots_values, instructions, test)
        print('The result of 1st part of the 10th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(bots_values, instructions)
        print('The result of 2nd part of the 10th day of AoC is: ' + str(result_part_2))
