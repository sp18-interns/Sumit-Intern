# year = int(input('Enter the year: '))
# # b = int(a)
# # if  b  %  4 == 0:
# #     print ('True')
# # else :
# #     print ('False')
def is_leap(year):
     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap(year))
