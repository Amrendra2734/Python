fpath=input('Enter the file path: ')
try: 
    fhand = open(fpath)
except:
    print('File not found in the given path: ',fpath)
    quit()
#Now you can do any work with fhand freely as if you get a wrong path, the program will quit itself.
for line in fhand:
    if not line.startswith('My'):
        continue
    print(line)