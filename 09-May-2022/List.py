# list nesting

list_1 = [1,2,3,'e']
list_2 = [4,5,6,'f']
list_3 = ['a','b','c','g']
list_4 = ['w','x','y','z']

sumit = [list_1,list_2,list_3,list_4]
print (sumit)

first = [row[0]for row in sumit]
second = [row[1]for row in sumit]
third = [row[2]for row in sumit]
fourth = [row[3]for row in sumit]

matrix_2 = [first, second, third, fourth]
print(matrix_2)