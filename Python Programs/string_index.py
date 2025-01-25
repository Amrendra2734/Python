fruit='Banana'
print('The 2nd charcter of the string fruit is:',fruit[2])                        #You can extract character from strings using index operator []
length = len(fruit)                                                                #You can get the length of the string using len()
print("Length of fruit:",length)
#using for loop, Definite loop
print('For')
index = 0
for i in fruit:
    print(index,i)
    index+=1
 #using while loop , Indefinite loop
print("While")
index = 0
while index < len(fruit):
    print(index,fruit[index])
    index+=1
