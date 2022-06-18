def rotate(lst, k):
    return lst[-k:] + lst[:-k]
l = [2, 3, 7, 0]
print(rotate(l, 2))