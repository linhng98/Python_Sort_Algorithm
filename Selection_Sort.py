import time


def selection_sort(Array):
    for i in range(len(Array) - 1):
        min_index = i
        for j in range(i + 1, len(Array)):
            if Array[j] < Array[min_index]:
                min_index = j
        Array[i], Array[min_index] = Array[min_index], Array[i]


def main():
    Array = [48, 16, 70, 66, 57, 71, 77, 6, 64, 74, 73, 90, 83, 56, 97]
    start = time.time()
    selection_sort(Array)
    end = time.time()
    print(Array)
    print(end - start)


if __name__ == '__main__':
    main()
