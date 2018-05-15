def subsets(array):
    """
        Generate all possible subsets from a given array.
    """
    if(array == []):
        return [[]]

    inner = subsets(array[1:])
    current = list(map(lambda i: i + [array[0]], inner))
    return inner + current


def max_after_all_operations(n, operations):
    """
    https://wcipeg.com/wiki/Prefix_sum_array_and_difference_array
    Inputs:
    n -- int: size of array
    operations -- array of arrays of a, b, k:
        For every operation:
            increment all elements in array between, 
                * a and b inclusive
                * index starting at 1

    At the end of this operation = [1, 2, 100], n = 5 we would have
    array = [100, 100, 0, 0, 0]

    Output:
    int max(array)
    """
    arr = (n + 1) * [0]
    for a, b, k in operations:
        arr[a - 1] += k
        arr[b] -= k
    
    max = 0
    tmp = 0
    for diff in arr:
        tmp += diff
        if tmp > max:
            max = tmp

    return max 