# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true
from src.data_structures import stack


def are_balanced(paren1, paren2):
    input = (paren1, paren2)
    if(
        (input == ('[', ']')) or
        (input == ('{', '}')) or
        (input == ('(', ')'))
    ):
        return True

    return False


def is_closing_paren(char):
    return char in "}])"


def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    if (len(s) == 0):
        return True
    elif(len(s) % 2 == 1):
        return False

    stk = stack.Stack()
    stk.push(s[0])

    for char in s[1:]:
        if(is_closing_paren(char)):
            if(are_balanced(stk.peek(), char)):
                stk.pop()  # close paren
            else:
                return False  # can't close -- fail
        else:
            stk.push(char)  # open paren

    is_valid = stk.peek() == None
    return is_valid
