data = 'From amrendra.xxxxxxxxxx@kiet.edu Sat Jan 5 09:14:16 2024'
atpos = data.find('@')                 # finds the @ as you want to print the host name.
spos = data.find(' ',atpos)            #finds the first space after '@' 
college = data[atpos+1 : spos]         
print(college)