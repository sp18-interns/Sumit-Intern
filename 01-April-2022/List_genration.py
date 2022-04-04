

import glob
import os

os.chdir(r'D:\500 gbdata\Software')
my_files = glob.glob('*.*')
print(my_files)
print(my_files, file=open('list.txt', 'a'))