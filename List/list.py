nums = [1,2,3,4,5]
strings = ['Hello','World']
lists = [[1,2,3],[4,5,6]]
lst = [1,'Hello',[4,5,6]]
print(nums,'\n',strings,'\n',lists,'\n',lst)
#List are mutable
nums[2]= 777
print(nums)
#print length of list
print(len(nums))
#making list using range 
range10 = range(10)
print(type(nums),type(range10))           #<class 'list'> <class 'range'>
print(range(10))                         #range(0, 10)
for i in range(10):                      #0 t0 9
    print(i)