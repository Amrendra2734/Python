filepath = input("Enter filepath: ")
count = dict()
if len(filepath)<1:
    fhandle = open("C:\\Users\\HP\Desktop\\Git repositories\\Python\File handling\\intro-short.txt")
else:
    fhandle = open(filepath)



for line in fhandle:
    # line = line.rstrip()            #No use currently
    wds = line.split()
    for wd in wds:
        count[wd]=count.get(wd,0)+1

#SWAPPPING KEY VALUE PAIRS
swap = list()
for v,k in count.items():
    swap.append((k,v))

print("\n*************SORTING.......*****************\n")
swap = sorted(swap,reverse=True)
final = list()
for v,k in swap:
    final.append((k,v))
print("\n*************SORTED LIST*****************\n")
print(final)
Final = dict(final)
print("\n*************SORTED DICTIONARY*****************\n")
print(Final)
print("\n*************MOST COMMON WORD*****************\n")
print(next(iter(Final.items())))         #Prints the first key value pair