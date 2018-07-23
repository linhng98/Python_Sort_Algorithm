import time


def heapify(Array, start_index, end_index):
    largest_index = start_index
    left = start_index * 2 + 1
    right = start_index * 2 + 2

    if left <= end_index and Array[left] > Array[largest_index]:
        largest_index = left
    if right <= end_index and Array[right] > Array[largest_index]:
        largest_index = right
    if largest_index != start_index:
        Array[largest_index], Array[start_index] = Array[start_index], Array[largest_index]
        if largest_index <= int((end_index - 1) / 2):
            heapify(Array, largest_index, end_index)


def heap_sort(Array):
    end_index = len(Array) - 1
    for i in range(int((end_index - 1) / 2), -1, -1):
        heapify(Array, i, end_index)

    for i in range(end_index, 0, -1):
        Array[i], Array[0] = Array[0], Array[i]
        heapify(Array, 0, i - 1)


def main():
    Array = []
    for i in range(1000, 0, -1):
        Array.append(i)
    start = time.time()
    heap_sort(Array)
    end = time.time()
    print(Array)
    print(end - start)


if __name__ == '__main__':
    main()

