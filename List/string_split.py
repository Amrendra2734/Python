fpath = r'C:\Users\HP\Desktop\Git repositories\Python\File handling\Hello.txt' 
fhand = open(fpath)
lst = list()
for line in fhand:
    line=line.rstrip()
    lst.append(line)              #made a list that has lines from the file as elements.
print(lst)
intro = lst[0]
str2 = lst[1]
str3= lst[3]
#String splitting
string_list= intro.split()
print(string_list)

#Double splitting pattern  to get the host name of my email.

elist = str3.split()       #had  My email is amrendraranchi.27@gmail.com so made a list using split
print(elist)
email= elist[3]            #made a string of my email
print(email)


again = email.split('@')   #then split again with parameter '@' to make another list.

print(again[1])            #printed my host name