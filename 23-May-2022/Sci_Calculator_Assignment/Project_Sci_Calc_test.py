from Project_Sci_Calc import Calculator
import math
import time

while True:
    n1 = int(input('Enter the first number for calculation : '))
    n2 = int(input('Enter the second number for calculation : '))
    calc = Calculator(n1, n2)
    choice = " "
    print('''       Here is list of Calculation :-
            1 : ADD       ||  2 : SUBTRACTION  ||  3 : MULTIPLICATION
            4 : DIVISION  ||  5 : SIN RADIAN   ||  6 : COS RADIAN
            7 : TAN RADIAN
            0 : Exit''')
    try:
        choice = int(input('Enter the number of your choice : '))

    except:
        print('Enter the valid number : ')
    if choice == 1:
        print(n1, '+', n2, '=', (calc.addition()))
        time.sleep(2)
    elif choice == 2:
        print(n1, '-', n2, '=', (calc.substraction()))
        time.sleep(2)
    elif choice == 3:
        print(n1, '*', n2, '=', (calc.multiplication()))
        time.sleep(2)
    elif choice == 4:
        print(n1, '/', n2, '=', (calc.division()))
        time.sleep(2)
    elif choice == 0:
        break
