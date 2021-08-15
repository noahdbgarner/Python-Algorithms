from structures.structures import *

def max_number_of_k_sum_pairs(nums, k: int) -> int:
    """
    Description:
        Return the maximum number of operations you can perform on an array where 2 numbers
        sum to k. Each time a pair sums to k, remove them from the list, and increment the counter

    Args:

    Returns:

    Explanation:

    Edge Cases:

    Complexity Analysis:
        Space: O(n)
        Time: O(n)
    """

    counter = 0
    occurrences = {}
    for num in nums:
        # As the list is iterated, we should see this difference in the occurrences dict
        difference = k - num
        # Remove 1 occurrence and increment counter if occurrences contains the difference
        if occurrences.get(difference, 0):
            occurrences[difference] -= 1
            counter += 1
        else:
            # Create a key of num if it does not exist, and increment its occurrences value
            occurrences[num] = occurrences.get(num, 0) + 1
    return counter



if __name__ == "__main__":


    print(max_number_of_k_sum_pairs(int_list, k=15))

