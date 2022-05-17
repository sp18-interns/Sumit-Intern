x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# initialize tuple
myTuple = (True, 50000, 'Bajaj')

# tuple to list
myList = list(myTuple)



myList[1] = 10000

myTuple1 = tuple(myList)

print(type(myTuple1))