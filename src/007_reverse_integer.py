# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store
# integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    s = str(x)
    is_negative = s.startswith('-')
    min_return_value = -2**31
    max_return_value = 2**31 - 1

    solution = -int(s[1:][::-1]) if(is_negative) else int(s[::-1])
    
    if min_return_value <= solution <= max_return_value:
        return solution
    
    return 0