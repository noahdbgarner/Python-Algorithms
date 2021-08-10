from time import sleep
import random
from typing import List
from test_structures import Structures

'''
Title:
    Longest Substring Without Repeating Characters
    Sliding window optimized solution
Description:
    Use a sliding window with a map that maps characters to an index. Thus, we can immediately skip the
    characters immediately when we found a repeated character
Complexity Analysis:
    Space: O(m|n)
    Time: O(m|n)
'''

def length_of_longest_substring(s: str) -> int:
    # unique char string, max unique char string
    ucs, mucs = "", ""
    for i in range(len(s)):
        if s[i] not in ucs:
            ucs += s[i]
        else:
            if len(mucs) < len(ucs):
                # Save our cur_max
                mucs = ucs
            # updates the unique char string by dropping everything before and including the repeated
            # char. Since an index starts at 0, and we want to include this in the drop, we must add 1
            # then we append the repeated char to the new string
            ucs = ucs[ucs.index(s[i]) + 1:] + s[i]

    return max(len(mucs), len(ucs))


'''
Misc Method
'''
def print_random_slices(words: List[str]) -> None:
    # Like lists, we can enumerate strings, then we can easily slice them at all indices
    while(True):
        word = random.choice(words)
        for index, curchar in enumerate(word):
            print(word[:index]+curchar)
            sleep(.01)

        for index, curchar in enumerate(word):
            print(word[index:])
            sleep(.01)




if __name__ == "__main__":


    print_random_slices(Structures.string_list)









