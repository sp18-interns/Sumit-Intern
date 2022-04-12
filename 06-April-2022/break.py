list_1 = ['Abrar', 'Yash', 'Sumit', 'Chirag', 'Mukesh', 'Parag']  
list_2 = ['Good', 'best']  
for i in list_1:  
    for j in list_2:  
        print(i, j)  
        if i == 'Parag' and j == 'best':  
            print('BREAK')  
            break  
    else:  
        continue  
    break