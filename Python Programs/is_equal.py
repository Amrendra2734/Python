print(5==5.0)     #True

print(5 is 5.0)  #False as it's memory location is different.
a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)    #Is false , they are in different memory location
c= (1,2,3)
d= (1,2,3)
print(c==d)     #True  
print(c is d)   #True as tupple are immutable they are stored in the same memory location.