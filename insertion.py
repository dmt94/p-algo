# sort in ascending order by repeatedly comparing each element
# with the values before it, and inserting the current element (stored as temp_val) to the right of a value if that value is less than it/ temp_val.

def insertion_sort(arr):
    for index in range(1, len(arr)):
        # starts by iterating over the element at index 1 in outer loop
        # store the current value in outer loop into the variable temp_val
        temp_val = arr[index]
        position = index - 1
        # set position to an index value before the current value (temp_val)
        # this represents the "left" of the current value

        while position >= 0:
            # inner loop functionality is to keep comparing every value to the left of the current value stored in temp_val until we encounter a value that is less than temp_val

            # conditional statement compares the current temp_val to the value immediately before it at the index value stored in position
            if arr[position] > temp_val:
                # if the value before temp_val is greater than temp_val,
                # this value then shifts to the right indicated as arr[position + 1]
                arr[position + 1] = arr[position]

                # to continue comparing the temp_val to the values before it, 
                # position is decremented by 1, continuing the while loop of comparison 
                # until we encounter a value that is less than the temp_val
                position = position - 1
            else:
                break
        #if a value is encountered to be less than the temp_val, then temp_val is then 
        #given a new position to the right of that value, sorting it in its right position
        arr[position + 1] = temp_val
    return arr

