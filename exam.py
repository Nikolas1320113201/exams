def newMax(lst):
    max = lst[0]
    for k in range(1, len(lst)):
        if lst[k] > max:
            max = lst[k]
    return max

print(newMax([1,5,7,2,9]))
