import random
from test_structures import Structures



'''
Title: 
    Max Number of K-Sum Pairs: Inspired by "Two Sum To a Target"
Description:
    Return the maximum number of operations you can perform on an array where 2 numbers
    sum to k. Each time a pair sums to k, remove them from the list, and increment the counter
Complexity Analysis:
    Space: O(n)
    Time: O(n)
'''
def maxOperations(nums, k: int) -> int:
    counter = 0
    occurances = {}
    for num in nums:
        # As the list is iterated, we should see this difference in the occurrences dict
        difference = k - num
        # Remove 1 occurrence and increment counter if occurrences contains the difference
        if occurances.get(difference, 0):
            occurances[difference] -= 1
            counter += 1
        else:
            # Create a key of num if it does not exist, and increment its occurrences value
            occurances[num] = occurances.get(num, 0) + 1
    return counter



if __name__ == "__main__":

    int_list = Structures.int_list
    long_string = Structures.long_string

    print(maxOperations(int_list, k=15))


    print(long_string[3:])