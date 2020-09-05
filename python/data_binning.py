input1 = [0, 4, 12, 16, 16, 18, 24, 26, 28]
input2 = [2, 6, 7, 9, 13, 20, 21, 25, 30]
input3 = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215]


def main():
    print(f"Equal width of input1 is {equal_width(input1, 3)}\n")
    print(f"Equal frequency of input1 is {equal_frequency(input1, 3)}\n")
    print(f"Equal width of input2 is {equal_width(input2, 3)}\n")
    print(f"Equal frequency of input2 is {equal_frequency(input2, 3)}\n")
    print(f"Equal width of input3 is {equal_width(input3, 3)}\n")
    print(f"Equal frequency of input3 is {equal_frequency(input3, 3)}\n")


def equal_width(arr, k):
    min_arr = min(arr)
    w = int((max(arr)-min_arr)/k)   #Width of the interval
    result = []
    boundaries = []
    for i in range(0, k+1):
        boundaries = boundaries + [min_arr + w * i]
    for i in range(0,k):
        tmp = []
        for j in arr:
            if arr[i] < j < arr[i + 1]:
                tmp += [j]
        result += [tmp]
    return result


def equal_frequency(arr, k):
    length = len(arr)
    n = int(length/k)   #Number of elements per bin
    result = []
    for i in range(0, k):
        tmp = []
        for j in range(i * n, (i + 1) * n):
            if j >= length:
                break
            tmp = tmp + [arr[j]]
        result.append(tmp)


if __name__ == '__main__':
    main()
