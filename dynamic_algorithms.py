
def maxOperations(nums, k: int) -> int:
    counter = 0
    occurances = {}
    for num in nums:
        # As the list is iterated, we should see this difference in the occurances dict
        difference = k- num
        # Remove 1 occurance and increment counter if occurances contains the difference
        if occurances.get(difference, 0):
            occurances[difference] -= 1
            counter += 1
        else:
            # Create a key of num if it does not exist, and increment its occurances value
            occurances[num] = occurances.get(num, 0) + 1
    return counter





def main():



    print(maxOperations(nums=[1,2,3,4,5,6,7,8,9,0,10,20,10,2,3,4,5,6,11], k=15))


    return

if __name__ == "__main__":
    main()