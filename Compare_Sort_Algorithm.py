import time
import sys


def bubble_sort(Array):
    for i in range(len(Array) - 1):
        swapped = False
        for j in range(len(Array) - i - 1):
            if Array[j] > Array[j + 1]:
                Array[j], Array[j + 1] = Array[j + 1], Array[j]
                swapped = True
        if swapped is False:
            break


def selection_sort(Array):
    for i in range(len(Array) - 1):
        min_index = i
        for j in range(i + 1, len(Array)):
            if Array[j] < Array[min_index]:
                min_index = j
        Array[i], Array[min_index] = Array[min_index], Array[i]


def insertion_sort(Array):
    for i in range(1, len(Array)):
        temp_var = Array[i]
        j = i - 1
        while j >= 0 and Array[j] > temp_var:
            Array[j + 1] = Array[j]
            j = j - 1
        Array[j + 1] = temp_var


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
        heapify(Array, largest_index, end_index)


def heap_sort(Array):
    end_index = len(Array) - 1
    for i in range(end_index, -1, -1):
        heapify(Array, i, end_index)

    for i in range(end_index, 0, -1):
        Array[i], Array[0] = Array[0], Array[i]
        heapify(Array, 0, i - 1)


def partition(Array, low, high):
    i = low - 1
    pivot = Array[high]

    for j in range(low, high):
        if Array[j] <= pivot:
            i += 1
            Array[i], Array[j] = Array[j], Array[i]
    Array[i + 1], Array[high] = Array[high], Array[i + 1]
    return i + 1


def quick_sort(Array, low, high):
    if low < high:
        pi = partition(Array, low, high)
        quick_sort(Array, low, pi - 1)
        quick_sort(Array, pi + 1, high)


def merge(Array, left, mid, right):
    amount_element_left_array = mid - left + 1
    amount_element_right_array = right - mid

    left_array = [0] * amount_element_left_array
    right_array = [0] * amount_element_right_array

    for i in range(amount_element_left_array):
        left_array[i] = Array[i + left]
    for j in range(amount_element_right_array):
        right_array[j] = Array[j + mid + 1]

    i = 0
    j = 0
    k = left

    while i < amount_element_left_array and j < amount_element_right_array:
        if left_array[i] < right_array[j]:
            Array[k] = left_array[i]
            i += 1
        else:
            Array[k] = right_array[j]
            j += 1
        k += 1

    while i < amount_element_left_array:
        Array[k] = left_array[i]
        i += 1
        k += 1
    while j < amount_element_right_array:
        Array[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(Array, left, right):
    if left < right:
        mid = int((left + right - 1) / 2)
        merge_sort(Array, left, mid)
        merge_sort(Array, mid + 1, right)
        merge(Array, left, mid, right)


def generate_array():
    Array = []
    for i in range(1000, 0, -1):
        Array.append(i)
    return Array


def count_time_sort_function(sort_func, Array, name_func):
    start = time.time()
    sort_func(Array)
    end = time.time()
    print('{0} time : {1}'.format(name_func, end - start))


def main():
    sys.setrecursionlimit(1500)

    Array = generate_array()
    count_time_sort_function(selection_sort, Array, 'selection sort')

    Array = generate_array()
    count_time_sort_function(insertion_sort, Array, 'insertion sort')

    Array = generate_array()
    count_time_sort_function(bubble_sort, Array, 'bubble sort')

    Array = generate_array()
    count_time_sort_function(heap_sort, Array, 'heap sort')

    Array = generate_array()
    start = time.time()
    quick_sort(Array, 0, len(Array) - 1)
    end = time.time()
    print('{0} time : {1}'.format('quick sort', end - start))

    Array = generate_array()
    start = time.time()
    merge_sort(Array, 0, len(Array) - 1)
    end = time.time()
    print('{0} time : {1}'.format('merge sort', end - start))


if __name__ == '__main__':
    main()
