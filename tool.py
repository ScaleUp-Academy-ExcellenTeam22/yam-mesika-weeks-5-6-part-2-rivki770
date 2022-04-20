def interleave(*collection_of_iterables):
    """
     A function that receives a list of lists and returns a merge between the lists.
     (merge: the first object of all, the second object of all...)
     For example:
        input: 'abc', [1, 2, 3], ('!', '@', '#').
        output: 'a', 1, '!', 'b', 2, '@', 'c', 3, '#'

    :param collection_of_iterables: Unlimited list of objects, any object is type of iterable.
    :return: In each reading the object in the next position
    """
    minimum_collection_size = min(len(iterable) for iterable in collection_of_iterables)
    current_index = 0
    while current_index < minimum_collection_size:
        for iterable in collection_of_iterables:              # move on all a list
            yield iterable[current_index]
        current_number += 1


def main():
    #example_1
    print([p for p in interleave('abc', [1, 2, 3], ('!', '@', '#'))])

    #example_2
    print([p for p in interleave('abc', [1, 2], ('!', '@', '#'))])

    #example_3
    print([p for p in interleave('abc', [1, 2, 3], ('!', '@', '#'), 'XYZ')])


if __name__ == '__main__' :
    main()