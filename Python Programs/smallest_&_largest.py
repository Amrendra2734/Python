S=[23.55,5,78,8,98,65,4,3]
smallest = None             # Initialised the smallest and largest to None value to later assign them the first value for proper searching.
largest = None
for i in S:
    if smallest is None:   #"is" is similar to '==' and implies "is same as" and there's "is not" which is similar to !=.
        smallest = i      #assigning them First value.
        largest = i
    elif smallest > i:
        smallest = i
    if largest < i:     #Both ifs are executed , but if I putted elif then it would'nt work like this.
        largest = i
print('Smallest is:',smallest,'and largest is:',largest)