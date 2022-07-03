import textwrap

python_desc = """Python is a general-purpose interpreted, interactive, object-oriented, 
                 and high-level programming language. It was created by Guido van Rossum 
                 during 1985- 1990. Like Perl, Python source code is also available under 
                 the GNU General Public License (GPL). This tutorial gives enough 
                 understanding on Python programming language."""

my_wrap = textwrap.TextWrapper()
wrap_list = my_wrap.wrap(text=python_desc)

for line in wrap_list:
    print(line)

single_line = """Python is a general-purpose interpreted, interactive, object-oriented, 
                 and high-level programming language."""

print('\n\n' + my_wrap.fill(text=single_line))


class TextWrapper:
    pass