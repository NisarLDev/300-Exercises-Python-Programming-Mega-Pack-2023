import sys

 # My solution

learning = "I am learning "
py = "Python "
vers = "version "
version_py = ".".join(map(str, sys.version_info[:2]))
print(learning+py+vers+version_py)

# Solution of the instructor

lang = 'Python'
version = '3.8'
print(f'I am learning {lang} version {version}')
