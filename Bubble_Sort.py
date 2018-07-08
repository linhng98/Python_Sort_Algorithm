import time


def bubble_sort(Array):
    for i in range(len(Array) - 1):
        swapped = False
        for j in range(len(Array) - i - 1):
            if Array[j] > Array[j+1]:
                Array[j], Array[j+1] = Array[j+1], Array[j]
                swapped = True
        if swapped is False:
            break


def main():
    Array = [48, 16, 70, 66, 57, 71, 77, 6, 64, 74, 73, 90, 83, 56, 97]
    start = time.time()
    bubble_sort(Array)
    end = time.time()
    print(Array)
    print(end - start)


if __name__ == '__main__':
    main()
