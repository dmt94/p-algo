numbers = [13,24,5,1,27,12,4,44]

def bubble_sort(list_a):
    indexing_length = len(list_a) - 1
    # I declared indexing_length with -1 because we only want to compare the values inside the list, this limits our scope of comparison

  
    sorted = False
    # this is a local variable that will be used throughout this function
    # this will be used inside the control flow to break out from loop once the list has been sorted

    while not sorted:
    # as long as the sorted variable is False
        sorted = True

        for i in range(0, indexing_length):
            # we are targeting the indexing_length variable 
            if list_a[i] > list_a[i+1]:
                #we are comparing the value from the left to the value to the right at each position iterated
                # within this loop, we compare each pair adjaent values and swap those values if they're out of order and switch sorted to Talse
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                #what we are saying here is if the value to the left is greater than the value to the right, then the values switch
    #once all items have been sorted, the if statement won't activate and the sorted variable will remain True, which will break the while loop
    return list_a


print(bubble_sort(numbers))