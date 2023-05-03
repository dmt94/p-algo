# Time Complexity of O(N)
def greatestNumber(arr):
    greatest = float('-inf')
    for i in range(len(arr)):
      if arr[i] > greatest:
         greatest = arr[i]
    return greatest

def lowestNumber(arr):
    lowest = float('inf')
    for i in range(len(arr)):
      if arr[i] < lowest:
         lowest = arr[i]
    return lowest


print(greatestNumber([4,3,2,1000,4,5,233]))
print(lowestNumber([4,3,2,1000,4,5,233]))