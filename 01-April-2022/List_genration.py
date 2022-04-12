

import glob
import os

os.chdir(r'D:\Spark Eighteen\Complete Python Bootcamp Go from zero to hero in Python 3\[Tutsgalaxy.com] - Complete Python Bootcamp Go from zero to hero in Python 3')
my_files = glob.glob('*.*')
print(my_files)
print(my_files, file=open('list1.txt', 'a'))