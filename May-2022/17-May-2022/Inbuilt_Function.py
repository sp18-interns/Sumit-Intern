# program to display the namespace of imported built-in module
# or import a module and display its namespace

import copy
import os
for name in copy.__dict__:
    print(name)

for name in os.__doc__:
    print( name)