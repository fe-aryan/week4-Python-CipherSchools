import pdb # import pdb module
# module - python file contains usefull classes and functions wrote by developer  

# According to wikipedia - Debugging is the process of finding and resolving defects or problems within a computer program that prevent correct operation of computers software or a system.

# why debugging 
# 1.) our program is not running and causing unexpected errors.
# 2.) our program is working fine but not working the same way we want .




## steps for debugging 
# 1) set trace 
# 2) execute code line by line



pdb.set_trace()
name = input('your name :')
age = input('your age :')
print(f'hello {name} your age is {age}')
age2 = int(age) + 5
print(f'{name} you will be {age2} in next five years')


#  l
# c 
# q

