prime = [2,3,5]
a = int(input("Enter a number: "))
for i in prime:
    while a%i==0:
        a = a/i
if a==1:
    print("Number is ugly  ")
else:
    print("number not ugly")