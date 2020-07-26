import random

# Binary Search on unsorted list. Not really useful, but an interesting thought experiment


def binary_search(lst, elem):
    max = len(lst)
    min = 0
    return recursive_search(lst, elem, min, max)


def recursive_search(lst, elem, min, max):
    pointer = int((min+max)/2)
    candidate = -1

    if lst[pointer] == elem:
        return pointer

    candidate = recursive_search(lst, elem, pointer, max)
    if candidate != -1:
        return candidate
    candidate = recursive_search(lst, elem, min, pointer)
    if candidate != -1:
        return candidate
    return -1


def simple_test():
    awnser = random.randint(0, 19)
    test_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    test_list.insert(awnser, 1)
    print(awnser)
    print(binary_search(test_list, 1))


simple_test()
