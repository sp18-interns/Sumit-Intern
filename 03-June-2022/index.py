# Replace Values in a List using Slicing

# define list
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']

# find the index of Rahul
i = l.index('Rahul')

# replace Rahul with Shikhar
l = l[:i] + ['Shikhar'] + l[i + 1:]

# print list
print(l)