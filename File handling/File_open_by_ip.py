# fpath=input('Enter the file path: ')              
fpath = r'C:\Users\HP\Desktop\Git repositories\Python\File handling\Hello.txt'       #Use r to deal with \ in string
print(fpath)
fhand = open(fpath)
#A simple program to print every line in a file
for i in fhand:          #i is the iteration integer which in this case , contains lines.   
    i=i.rstrip()
    print(i)

fhand.seek(0)      #To reset the handle to start.
#counting lines
count = 0 
for line in fhand:
    count+=1
print('The number of lines are:',count)