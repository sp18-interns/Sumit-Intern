

import glob
import os

os.chdir(r'D:\Spark Eighteen\Daily Commit\Sumit-Intern\13-April-2022')
my_files = glob.glob('*.*')
print(my_files)
print(my_files, file=open('list1.txt', 'a'))