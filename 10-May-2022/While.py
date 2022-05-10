# code 1

i = 3

while True:
 i = i - 1
 print(i)
 if i == 0:
   break


#code 2

x = 8

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
    else:
        print('continuing...')
        continue