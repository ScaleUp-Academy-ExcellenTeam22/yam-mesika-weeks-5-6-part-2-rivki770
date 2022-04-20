def state_in_line_on_keyboard(path_to_file_of_country: str):
    """
    A function that gets a path to a file with countries,
    and searches for a country that can be written using letters from a single line of the keyboard.
    :param path_of_file_of_country: path to file of states.
    :return: nothing.
    """
    first_keyboard_row = set('qwertyuiop\n')
    second_keyboard_row = set('asdfghjkl\n')
    third_keyboard_row = set('zxcvbnm\n')

    try:
        with open(path_to_file_of_country, "r") as file_states:
            for state in file_states:
                state_set = set(state)
                if len(set(state_set.difference(first_keyboard_row))) == 0:
                    print(f'In row 1: {state}')
                    return
                elif len(set(state_set.difference(second_keyboard_row))) == 0:
                    print(f'In row 2: {state}')
                    return
                elif len(set(state_set.difference(third_keyboard_row))) == 0:
                    print(f'In row 3: {state}')
                    return
    except IOError:
        print('Error while opening the file!')


def main():
    state_in_line_on_keyboard("C:\\rivki\\studies\\YearD\\SemesterB\\Excellent\\Python\\HW_1\\Git\\yam-mesika-weeks-5-6-rivki770\\states.txt")


if __name__ == '__main__' :
    main()