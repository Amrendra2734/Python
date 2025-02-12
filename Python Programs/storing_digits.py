a = int(input())
b = int(input())
if a>b:
	print("Invalid limits")
else:
	for num in range(a,b):
		digits = list()
		while num!=0:
			digits.append(num%10) 
			# print(num%10)
			num = int(num/10)
		print("**********NUMBER**************")
		print(digits)