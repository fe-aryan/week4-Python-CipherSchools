## w -->write    a--> append           r+    

# with open('file2.txt' , 'w') as f :
#     f.write("hello")



# with open('file2.txt' , 'a') as f :
#     f.write("\nthe war of its seremony")


with open('file2.txt' , 'r+') as f :
    f.seek(len(f.read()))
    f.write("please do it")






