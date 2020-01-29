x=int(input("enter a no."))
for i in range(1,x+1):
	if (i==1) or (i==x):
		print("*"*x)
	else:
		print("*" + " "*(x-2) + "*")	
		
