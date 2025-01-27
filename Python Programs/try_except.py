n= input("Enter a number: ")
try:
    N=int(n)                             #try runs this code and if it has any tracebacks then 
except:
    print("Not a number")                #instead of giving a traceback it runs this
print("Good JOb")