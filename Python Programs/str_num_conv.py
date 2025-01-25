istr = input("Enter a number: ")
type(istr)
try:
    Num=int(istr)   #Potential traceback code
except:
    Num = -1       #This is a kind of flag that says that something has gone wrong.
print("Number is:", Num)