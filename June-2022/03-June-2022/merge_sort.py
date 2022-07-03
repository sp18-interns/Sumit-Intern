def merge(L1, L2):
    L = L1 + L2
    return L


def merge_sort(L1, L2):
        L = L1 + L2
        L.sort()
        return L

L1 = [9, 12, 17, 25]
L2 = [3, 5, 11, 13, 16]
a = merge(L1, L2)
b = merge_sort(L1, L2)
print(a)
print(b)
