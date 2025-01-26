str = 'Amrendra Singh'
print('Before',str)
nstr = str.replace(' ',' Pratap ')        #finds all the ' ' and replaces it with 'Pratap'.
print('After',nstr)


#Let's say if you had ' Amrendra Singh '. There's 3 ' ' .
str = ' Amrendra Singh '
nstr = str.replace(' ',' Pratap ') 
print(nstr)                 #This will return Pratap Amrendra Pratap Singh Pratap, So to fix this.
nstr= str.strip()           #To remove trailing spaces. str.lstrip() will remove left spaces and str.rstrip() will remove right.
nstr = nstr.replace(' ',' Pratap ')     
print(nstr)


#Also , str.replace( 'string1', 'replacement',n) where n is the number of replacement.
str2= 'ho ho ho ho ho'
nstr2 = str2.replace('ho','ha',2)       #replaces only two 'ho' with 'ha'..... ha ha ho ho ho
print(str2)
print(nstr2)



#You can also search prefixes and suffixes using str1.startswith(str2) and str1.endswith(str2)
line = 'Welcome to my abode'
print(line.startswith('Wel'))
print(line.startswith('wel'))         # Will return false as it is casesensitive.
print(line.endswith('abode'))