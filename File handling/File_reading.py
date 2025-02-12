fpath = r'C:\Users\HP\Desktop\Git repositories\Python\File handling\Hello.txt'       #Use r to deal with \ in string
print(fpath)
fhand = open(fpath)
read = fhand.read()
print(read)                 #prints everthing character by characters
print('The number of characters are:',len(read)) 