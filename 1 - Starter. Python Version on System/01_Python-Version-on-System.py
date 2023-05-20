import sys
 
 
print(sys.version.split()[0])

# OR

version = ".".join(map(str, sys.version_info[:3]))
print(version)
