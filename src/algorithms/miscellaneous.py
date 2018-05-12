def subsets(array):
    """
        Generate all possible subsets from a given array.
    """
    if(array == []):
        return [[]]

    inner = subsets(array[1:])
    current = list(map(lambda i: i + [array[0]], inner))
    return inner + current
