from structures.test_vars import *


def longest_substring_with_no_repeat_characters(s: str) -> int:
    """
    Description:
        Use a sliding window with a map that maps characters to an index. Thus, we can immediately skip the
        characters immediately when we found a repeated character

    Args:
        s (str): the input string

    Returns:
        max(len(mucs), len(ucs)) (int): the longest substring with no repeat characters

    Explanation:
        ucs = unique char string, mucs = max unique char string

        ucs = ucs[ucs.index(s[i]) + 1:] + s[i]
            updates the unique char string by dropping everything before and including the repeated
            char. Since an index starts at 0, and we want to include this in the drop, we must add 1
            then we append the repeated char to the new string

    Edge Cases:


    Complexity Analysis:
        Space: O(m|n) where...
        Time: O(m|n) where...
    """
    ucs, mucs = "", ""
    for i in range(len(s)):
        if s[i] not in ucs:
            ucs += s[i]
        else:
            if len(mucs) < len(ucs):
                mucs = ucs
            ucs = ucs[ucs.index(s[i]) + 1:] + s[i]

    return max(len(mucs), len(ucs))



if __name__ == "__main__":


    print(longest_substring_with_no_repeat_characters(long_string))









