import re


def find_matching_bracket(str, start_index):
    balance = 1
    i = start_index + 1
    while balance != 0:
        if i == len(str):
            break
        if(str[i] == "["):
            balance += 1
        if(str[i] == "]"):
            balance -= 1
        i += 1

    return i - 1


def decode_string(str):
    s = str
    match = re.search('\d+', s)
    if not match:
        return s

    result = ""

    while match:
        m = re.match('\D+', s)
        if(m):  # e.g. bracket contents = a2[ab] => we need to add the "a"
            result += m.group(0)

        n = int(match.group(0))
        left_bracket_index = match.span()[1]
        right_bracket_index = find_matching_bracket(s, left_bracket_index)
        bracket_contents = s[left_bracket_index + 1:right_bracket_index]
        decoded = n * decode_string(bracket_contents)
        result += decoded
        s = s[right_bracket_index + 1:]
        match = re.search('\d+', s)

    return result + s
