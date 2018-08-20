import time


class SortAlgorithm:

    # selection sort-----------------------------------------------------------
    @staticmethod
    def selection_sort(array):

        for i in range(len(array) - 1):
            min_index = i

            for j in range(i + 1, len(array)):
                if array[j] < array[i]:
                    min_index = j

            array[min_index], array[i] = array[i], array[min_index]

    # bubble sort -------------------------------------------------------------
    @staticmethod
    def bubble_sort(array):

        for i in range(len(array) - 1):
            swapped = False

            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True

            if swapped is False:
                break

    # insertion sort-----------------------------------------------------------
    @staticmethod
    def insertion_sort(array):

        for i in range(1, len(array)):
            key = array[i]
            j = i - 1

            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1

            array[j + 1] = key

    # heap sort----------------------------------------------------------------
    def heapify(self, array, start, end):
        if start < 0 or end > len(array) - 1:
            return
        else:
            largest = start
            left = start * 2 + 1
            right = start * 2 + 2

            if left <= end and array[left] > array[largest]:
                largest = left
            if right <= end and array[right] > array[largest]:
                largest = right
            if largest != start:
                array[largest], array[start] = array[start], array[largest]
                self.heapify(array, largest, end)

    def heap_sort(self, array):
        n = int((len(array) - 1) / 2)

        for i in range(n, -1, -1):
            self.heapify(array, i, len(array) - 1)

        for i in range(len(array) - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, 0, i - 1)

    # quick sort---------------------------------------------------------------
    @staticmethod
    def partition(array, start, end):
        i = start - 1
        pivot = array[end]

        for j in range(start, end):
            if array[j] < pivot:
                i += 1
                array[j], array[i] = array[i], array[j]

        array[end], array[i + 1] = array[i + 1], array[end]
        return i + 1

    def quick_sort(self, array, start, end):
        if start < end:
            pi = self.partition(array, start, end)
            self.quick_sort(array, start, pi - 1)
            self.quick_sort(array, pi + 1, end)

    # merge sort---------------------------------------------------------------
    @staticmethod
    def merge(array, left, mid, right):
        amount_arr_left = mid - left + 1
        amount_arr_right = right - mid

        arr_left = [0] * amount_arr_left
        arr_right = [0] * amount_arr_right

        for x in range(amount_arr_left):
            arr_left[x] = array[left + x]

        for y in range(amount_arr_right):
            arr_right[y] = array[mid + y + 1]

        i = 0
        j = 0
        k = 0

        while i < amount_arr_left and j < amount_arr_right:
            if arr_left[i] < arr_right[j]:
                array[left + k] = arr_left[i]
                i += 1
            else:
                array[left + k] = arr_right[j]
                j += 1
            k += 1

        while i < amount_arr_left:
            array[left + k] = arr_left[i]
            i += 1
            k += 1

        while j < amount_arr_right:
            array[left + k] = arr_right[j]
            j += 1
            k += 1

    def merge_sort(self, array, left, right):
        if left < right:
            mid = int((left + right) / 2)
            self.merge_sort(array, left, mid)
            self.merge_sort(array, mid + 1, right)
            self.merge(array, left, mid, right)

    # counting sort------------------------------------------------------------
    @staticmethod
    def counting_sort(array):
        max_value = max(array)
        result = [0] * len(array)
        counting_arr = [0] * max_value

        for i in array:
            counting_arr[i - 1] += 1

        k = 0
        for j in range(len(counting_arr)):
            while counting_arr[j] > 0:
                result[k] = j + 1
                counting_arr[j] -= 1
                k += 1

        for i in range(len(result)):
            array[i] = result[i]

    # radix sort---------------------------------------------------------------
    @staticmethod
    def count_sort_radix(array, exp):
        result = [0] * len(array)
        count = [0] * 10

        for i in range(len(array)):
            index = int((array[i] / exp)) % 10
            count[index] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for i in range(len(array) - 1, -1, -1):
            index = int((array[i] / exp)) % 10
            result[count[index] - 1] = array[i]
            count[index] -= 1

        for i in range(len(array)):
            array[i] = result[i]

    def radix_sort(self, array):
        max_number = max(array)
        exp = 1
        while max_number / exp > 0:
            self.count_sort_radix(array, exp)
            exp *= 10


"""
def main():
    sort = SortAlgorithm()
    array_demo = [48, 16, 70, 66, 57, 71, 77, 6, 64, 74, 73, 90, 83, 56, 97, 4]
    begin_time = time.time()
    sort.counting_sort(array_demo)
    finish_time = time.time()
    print(finish_time - begin_time)
    print(array_demo)


if __name__ == '__main__':
    main()
"""

sort_algorithm = SortAlgorithm()
selection = sort_algorithm.selection_sort
bubble = sort_algorithm.bubble_sort
insertion = sort_algorithm.insertion_sort
heap = sort_algorithm.heap_sort
quick = sort_algorithm.quick_sort
merge = sort_algorithm.merge_sort
counting = sort_algorithm.counting_sort
radix = sort_algorithm.radix_sort
