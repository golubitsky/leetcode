import random


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
