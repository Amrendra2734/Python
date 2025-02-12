fpath = r'C:\Users\HP\Desktop\Git repositories\Python\File handling\Hello.txt'       #Use r to deal with \ in string
print(fpath)
fhand = open(fpath)
for line in fhand:
    if line.startswith('My'):
        print(line)
#you can do the same thing using continue
fhand.seek(0)
for line in fhand:
    if not line.startswith('My'):
        continue
    print(line)