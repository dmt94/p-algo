a = [1,2,3]

def plus():
    for i in range (0, len(a)):
        print(a[i] + 1)

plus()


def sum():
    total = 0
    for i in range(0, len(a)):
        total += a[i]
    return total 

print(sum())


def pair():
    list_pair = []
    for i in range(0, len(a)): 
        current = a[i]
        current_list = []
        for j in range(0, len(a)):
            current_list.append([current, a[j]])
        list_pair.append(current_list)
        current_list = []
    return list_pair

print(pair())
        