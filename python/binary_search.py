import random

def binary_search(list, elem):
    max = len(list)
    min = 0
    return recursive_search(list, elem, min, max)


def recursive_search(list, elem, min, max):
    pointer = int((min+max)/2)
    if list[pointer] == elem:
        return pointer
    if pointer != max-1:
        upper_half = recursive_search(list, elem, pointer, max)
    if pointer != min:
        lower_half = recursive_search(list, elem, min, pointer)
    if upper_half != -1:
        return upper_half
    if lower_half != -1:
        return lower_half
    return -1


def simple_test():
    awnser = random.randint(0, 19)
    test_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    test_list.insert(awnser, 1)
    print(awnser)
    print(binary_search(test_list, 1))


simple_test()
