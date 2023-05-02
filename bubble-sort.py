numbers = [13,24,5,1,27,12,4,44]

def bubble_sort(list_a):
    indexing_length = len(list_a) - 1
    # I declared indexing_length with -1 because we only want to compare the values inside the list, this limits our scope of comparison

  
    sorted = False
    # this is a local variable that will be used throughout this function
    # this will be used inside the control flow to break out from loop once the list has been sorted

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a


print(bubble_sort(numbers))