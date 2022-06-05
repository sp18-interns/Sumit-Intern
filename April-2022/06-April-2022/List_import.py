from msilib.schema import File
from re import L


File = open('sumit.txt', 'r' )
f = File.readlines()
list_inp = f 
 
set_res = set(list_inp) 
print("The unique elements of the input list using set():")
list_res = (list(set_res))
  
for item in list_res: 
    print(item)
    print(item, file=open("unique.txt", 'a'))
#print (f)
#f.sort()
#print (f)
#b = len(f)
#print (b)

#number_of_unique_elements = len(set(f))
#number_of_elements = len(f)

#print("Number of elements in the list: ", number_of_elements)
#print("Number of unique elements in the list: ", number_of_unique_elements)

