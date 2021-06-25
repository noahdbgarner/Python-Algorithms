from time import sleep
import random
from typing import List
from test_structures import Structures






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









