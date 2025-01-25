# searching using booolean
found = False      # initialising boolean to false
num = 7
for i in [1,2,3,4,5,6,7,8,87]:
    if num==i:
        found=True #boolean set to True
        break     # Using break for less iterations.
if found==False:
    print('Not Found!!')
else:
    print('Found')