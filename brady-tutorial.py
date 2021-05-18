#This program sums a length 4 list into an accumulator named total, and prints the total at the end.



#this is our first function. Functions can be called repeatedly, anywhere
def list_sum(temp_list):
    accum = 0
    for i in range(0, len(temp_list)):
        accum = (accum + temp_list[i])
        print(accum)







list_of_lists=[[1,2,3,4], [8,9,3,4], [0,0,0,0], [-2,-2,-2,-2]]
for list in list_of_lists:
    list_sum(list)

