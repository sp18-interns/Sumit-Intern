def add(a, b) -> int:
    return a + b


a1 = add(1, 2)
print(a1)


def substract(a, b):
    return a - b


a2 = substract(2, 1)
print(a2)
print(a1 - a2)

s = input()

from collections import Counter

a = Counter(s)
print(a)
# if a['z'] * 2 == a['o']:
#     print("Yes")
# else:
#     print("No")
