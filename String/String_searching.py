str= 'Hello world'
print(str)
nstr= str.lower()           #Common practice of making the string to lower case for searching as it is case sensitive.
print(nstr)
pos = nstr.find('llo')      #Returns the index of first occurence.
print(pos)
pos1= nstr.find('l',5)      #Searche starts from index number 5 
print(pos1)               
z = nstr.find('z')          #returns -1 as it is not there.
print(z)
