import random

def binary_search(list, elem):
    max = len(list)
    min = 0
    return recursive_search(list, elem, min, max)


def recursive_search(list, elem, min, max):
    pointer = int(min+max/2)
    if list[pointer] == elem:
        return pointer
    elif min == max:
        return recursive_search(list, elem, pointer, max)
    else:
        return recursive_search(list, elem, min, pointer)


def simple_test():
    awnser = random.randint(0, 19)
    test_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    test_list.insert(awnser, 1)
    print(awnser)
    print(binary_search(test_list, 1))


simple_test()
