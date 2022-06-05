# def no_name(sumit = None):
#     if sumit == input(" "):
#         return no_name()
# sumit = " "
# print (sumit)
# #A code which accepts nothing & return string

def greet(name):
    # form
    print(f"Hello {name}, this is SP18")


greet('sumit')


# Program 2
def person(name):
    print(f"your RObo name is {name}")


person(name=1)


# Program 3
def sp18(tutor, student):
    print(f"{student} is mentored by {tutor}")


tutor = 'Abrar'
student = 'sumit'
print(sp18(tutor, student))
sp18(tutor='AbrarM', student='SumitS')


# Program 4
def Lunch(bread, dal, rice):
    return (f" today menu is {bread} with {dal} with {rice}")


bread = "Roti"
dal = "tadka"
rice = "steamed"
print(Lunch(dal, bread, rice))


# Program 5
def Lunch_2(toast, dal, rice):
    lunch_hour = f'your menu is {toast} , {dal} {rice}'
    return lunch_hour


person1 = (Lunch_2(1, 2, 3))
print(person1)


# Program 6
def smoke(cigrate, type):
    return f'Hello your brand is {cigrate}, {type}'


yash = smoke('Wills', 'Navycut')
sumit = smoke('wills', 'goldfalke')
print(yash, sumit)


# Program 7
def no_input(sp18='Hello interns'):
    sp18_firstday = (f'''hello {sp18} it is your first day ''')


print(no_input(sp18=""))


def greet1():
    return "My String"


print(greet1())