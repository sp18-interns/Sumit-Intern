from Project_Sci_Calc import Calculator
import time
import math

while True:
    n1 = int(input('Enter the first number for calculation : '))
    n2 = int(input('Enter the second number for calculation : '))
    calc = Calculator(n1, n2)
    choice = " "
    print('       Here is list of Calculation :-\n'
          '            1 : ADD       ||  2 : SUBTRACTION  ||  3 : MULTIPLICATION  || 4 : DIVISION\n'
          '            5 : SIN_rad   ||  6 : COS_rad      ||  7 : Tan_rad         || 8 : DEG to Rad\n'
          '            9 : RAD to DEG || 0 : Exit')
    try:
        choice = int(input('Enter the number of your choice : '))

    except:
        print('Enter the valid number : ')
    if choice == 1:
        print(n1, '+', n2, '=', (calc.addition()))
        time.sleep(2)
    elif choice == 2:
        print(n1, '-', n2, '=', (calc.subtraction()))
        time.sleep(2)
    elif choice == 3:
        print(n1, '*', n2, '=', (calc.multiplication()))
        time.sleep(2)
    elif choice == 4:
        print(n1, '/', n2, '=', (calc.division()))
        time.sleep(2)
    elif choice == 5:
        print(n1, 'Sin(Rad)', '=', (calc.sin_rad()))
        time.sleep(2)
    elif choice == 6:
        print(n1, 'Cos(Rad)', '=', (calc.cos_rad()))
        time.sleep(2)
    elif choice == 7:
        print(n1, 'Tan(Rad)', '=', (calc.tan_rad()))
        time.sleep(2)
    elif choice == 8:
        print('Degree of', 'Radian', n1, '=', (calc.deg_to_rad()))
        time.sleep(2)
    elif choice == 9:
        print('Radian of', 'Degree', n1, '=', (calc.rad_to_deg()))
        time.sleep(2)
    elif choice == 0:
        break
