def numbers_perfect_dish() -> int:
    '''
    The function check if sum of all the divisors of a certain number, is equal to the number itself,
    and return a number.
    (Perfect dish -> the sum of all the divisors of a certain number, is equal to the number itself).
    For example:
    6 is perfect dish: 1 + 2 + 3 = 6.
    8 is not perfect dish: 1 + 2 + 4 != 8.
    :return: The number that sum of all his divisions equal himself.
    '''
    number_to_check = 1
    while True:
        sum_list_of_divide = sum([i for i in range(1, number_to_check) if number_to_check % i == 0])
        if sum_list_of_divide == number_to_check:
            yield sum_list_of_divide
        number_to_check = number_to_check + 1


def main():
    perfect_dish_numbers = numbers_perfect_dish()
    while True:
        print(next(perfect_dish_numbers))


if __name__ == '__main__':
    main()
