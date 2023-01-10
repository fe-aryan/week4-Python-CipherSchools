# make function 'divide'
# divide(a,b)

# output ex:
# print(divide(4,2)) # 2
# print(divide(4,0)) # please don't divide by zero
# print(divide('4',2)) # please input numbers only

def divide(a,b):
    try: 
        return a/b
    except ZeroDivisionError :   
        print('you cannot divide a number by zero')
    except TypeError as err :
        # print("numbers must be int or floats") 
        print(err) 
    except:
        print("unexpected error")      

print(divide(10,0))
print(divide(10,"2"))