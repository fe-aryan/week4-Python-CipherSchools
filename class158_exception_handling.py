# Exception handling
# try ,except ,else ,  finally 

'''exception wo error hoti hh jaa hamare execution kk time pprr aati hai'''

# try:
#     age = int(input('Enter your age : ')) 
# except: 
#     print('invalid input')   

# if age < 18:
#     print('You can\'t play this game.')
# else:
#     print("you can play this game.") 




######### jbb tkk right input nhi denge,,tbb tkk chlta rhega , so we make code for that ...see below
while True:
    try:
        age = int(input('Enter your age : ')) 
        break
    except ValueError:
        print('maybe you entered string instead of number , try again')   
    except:
        print('unexcepted error')    

if age < 18:
    print('You can\'t play this game.')
else:
    print("you can play this game.") 

