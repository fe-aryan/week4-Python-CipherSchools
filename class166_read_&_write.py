with open('file2.txt','r') as rf:
    with open('file1.txt','w') as wf:
        wf.write(rf.read())


# in this code we have copy the files of 2 in 1 means we also re-write there         