"""A special number consists of each digit being even (202 is a special number, but 102 is not because 1 is odd in 102). Two 3-digit numbers 
 and 
 are given to John, and asked him to find all the special 3-digit numbers between them, including 
 """
a = int(input())
b = int(input())
if a>b or (a<100 and a>999 or b<100 or b>999 ):
	print("Invalid limits")
else:
	finals = list()
	for num in range(a,b+1):
		copy = num
		digits = list()
		while num!=0:
			digits.append(num%10) 
			# print(num%10)
			num = int(num/10)
		# print(digits)
		count = 0
		for i in digits:
			if i%2==0:
				count+=1
		if count == len(digits):
			finals.append(copy)
	if len(finals)<1:
		print("No Special Numbers exist")
	else:
		for i in range(len(finals)):
			if i==len(finals)-1:
				print(finals[i])
			else:
				print(finals[i],end=",")