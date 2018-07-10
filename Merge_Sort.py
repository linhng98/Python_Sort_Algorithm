import time


def merge(Array, left, mid, right):
    amount_left = mid - left + 1
    amount_right = right - mid

    left_array = [0] * amount_left
    right_array = [0] * amount_right

    for x in range(amount_left):
        left_array[x] = Array[x + left]
    for y in range(amount_right):
        right_array[y] = Array[y + mid + 1]

    i = 0
    j = 0
    k = left

    while i < amount_left and j < amount_right:
        if left_array[i] < right_array[j]:
            Array[k] = left_array[i]
            i += 1
        else:
            Array[k] = right_array[j]
            j += 1
        k += 1

    while i < amount_left:
        Array[k] = left_array[i]
        i += 1
        k += 1
    while j < amount_right:
        Array[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(Array, left, right):
    if left < right:
        mid = int((left + right) / 2)
        merge_sort(Array, left, mid)
        merge_sort(Array, mid + 1, right)
        merge(Array, left, mid, right)


def main():
    Array = [48, 16, 70, 66, 64, 57, 71, 77, 6, 74, 73, 90, 83, 56, 97]
    start = time.time()
    merge_sort(Array, 0, len(Array) - 1)
    end = time.time()
    print(Array)
    print(end - start)


if __name__ == '__main__':
    main()
