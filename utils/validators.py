""" Util containing validators used for Advent of Code

Author: Ic4r0 - https://github.com/Ic4r0

Created: 1st December 2021
"""


def check_valid_arguments(arguments_list: list[str]) -> (bool, int, int):
    """ Check if the inserted arguments are valid

    :param arguments_list: list of arguments
    :return: tuple containing a test flag, selected day and selected part
    """
    if len(arguments_list) > 0:
        if (len(arguments_list) == 3 and arguments_list[0] == 'test' and arguments_list[1].isnumeric() and
                arguments_list[2].isnumeric()):
            return True, int(arguments_list[1]), int(arguments_list[2])
        elif len(arguments_list) == 2 and arguments_list[0] == 'test' and arguments_list[1].isnumeric():
            return True, int(arguments_list[1]), None
        elif len(arguments_list) == 2 and arguments_list[0].isnumeric() and arguments_list[1].isnumeric():
            return False, int(arguments_list[0]), int(arguments_list[1])
        elif len(arguments_list) == 1 and arguments_list[0].isnumeric():
            return False, int(arguments_list[0]), None
        else:
            return None
    else:
        return None
