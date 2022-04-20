import math
import time


def average_runtime(list_or_set_of_words):
    """
    A function that receives a list of words and returns how long it takes on average to search for a specific word.
    :param list_or_set_of_words: A set or a list of words.
    :return: the average-time to find "zwitterion" in a set or a list
    """
    time_start = time.time()
    for i in range(0, 1000):
        if "zwitterion" in list_or_set_of_words:
            continue
    return (time.time() - time_start) / 1000


def open_file(path_to_file: str):
    """
    A function that gets a path to a file, and copies the words / text from the file to a list and a set,
    and it call to inner function that looking for a specific word in the list or set a function created.
    :param path_to_file: path to file.
    :return: nothing.
    """
    word_list = []
    word_set = set()

    try:
        with open(path_to_file, "r") as file:
            for word in file:
                word_list.append(word)
                word_set.add(word)
    except IOError:
        print('Error while opening the file!')

    print(f"The time for find zwitterion in list: {average_runtime(word_list)}")
    print(f"The time for find zwitterion in set: {average_runtime(word_set)}")


def main():
    open_file("C:\\rivki\\studies\\YearD\\SemesterB\\Excellent\\Python\\HW_1\\Git\\yam-mesika-weeks-5-6-rivki770\\words.txt")


if __name__ == '__main__':
    main()