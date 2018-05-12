import random
from src.data_structures.heap import MinHeap


def _merge(left, right):
    merged = []
    i_left = i_right = 0
    while(True):
        l_exists = i_left < len(left)
        r_exists = i_right < len(right)
        if(not l_exists and not r_exists):
            break

        l = r = False
        if(l_exists and r_exists):
            if(left[i_left] < right[i_right]):
                l = True
            else:
                r = True
        elif(l_exists):
            l = True
        elif(r_exists):
            r = True

        if(l):
            merged.append(left[i_left])
            i_left += 1
        if(r):
            merged.append(right[i_right])
            i_right += 1

    return merged


def merge_sort(arr):
    if(len(arr) <= 1):
        return arr

    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])

    return _merge(left, right)


def quick_sort(arr):
    if(len(arr) <= 1):
        return arr

    # split into left less than pivot, right greater than pivot
    pivot = random.randint(0, len(arr) - 1)
    left = []
    right = []
    for i in range(len(arr)):
        if(i == pivot):
            continue

        if(arr[i] <= arr[pivot]):
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [arr[pivot]] + quick_sort(right)


def selection_sort(arr):
    # don't modify the input; this whole method is silly,
    # but the point is heap_sort below
    input = arr.copy()
    sorted = []

    while(len(input)):
        m = min(input)
        sorted.append(m)
        input.remove(m)

    return sorted


def heap_sort(arr):
    """
    Skiena: "heapsort is nothing but an implementation of selection sort
        using the right data structure."
    """
    heap = MinHeap()
    for el in arr:
        heap.insert(el)

    sorted = []
    while(heap.size() > 0):
        sorted.append(heap.extract_min())

    return sorted
