## new chapter 
# built in errors 
# exception , how to handle them 
# raise your own errors , debugging , etc etc


# syntax error
# def func:
#     pass  

# name = "sumit"*


# Indentation error
'''indentation means spaces between codes ....or extra spaces  '''
# def funct():
#     print("hello")
#   print("world")  


# name error 
'''like jbb koi variable define nhi ho , means koi function define nhi ho ''' 
# print(funt())



# type error 
print(5 + "sumit")


# index error 
l = [1,2,3]
print(l[3])  #this is right syntax
print(l[5]) # ---> index error we get



# value error 
s = "abc"  # s="123"
print(int(s))


# attribute error 
l = [1,2,3]
l.push("12") # we got error,because push koi attribute he nhi hota list mai



# key error
d = {'name':'harshit'}
print(d['age'])

