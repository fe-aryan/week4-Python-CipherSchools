# readfile
# open function
# read method 
# seek method 
# tell method 
# readline method
# readlines method
# close method

f  = open("file1.txt")
print(f'cursor position - {f.tell()}')
# print(f.read())
# print(f.read())

print(f.readline(), ends= '')
print(f.readline())
print(f.readline())
f.close()

print(f.close())

