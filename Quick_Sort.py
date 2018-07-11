import time


def partition(Array, low, high):
    pivot = Array[high]
    i = low - 1

    for j in range(low, high):
        if Array[j] < pivot:
            i += 1
            Array[i], Array[j] = Array[j], Array[i]
    Array[high], Array[i + 1] = Array[i + 1], Array[high]

    return i + 1


def quick_sort(Array, low, high):
    if low < high:
        i = partition(Array, low, high)
        quick_sort(Array, low, i - 1)
        quick_sort(Array, i + 1, high)


def main():
    Array = [48, 16, 70, 66, 64, 57, 71, 77, 6, 74, 73, 90, 83, 56, 97]
    start = time.time()
    quick_sort(Array, 0, len(Array) - 1)
    end = time.time()
    print(Array)
    print(end - start)


if __name__ == '__main__':
    main()
