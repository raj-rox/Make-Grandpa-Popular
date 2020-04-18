import math
import random

def is2digit(n):
	if n<100 and n>0:
		return 1
	else:
		return 0

list1=[1,2,3,4,5,6,7,8,9]
copylist=[]
while(1):
	copylist=list1[:]
	n1=random.choice(copylist)
	a=10*n1
	copylist.remove(n1)
	n2=random.choice(copylist)
	a=a+n2
	copylist.remove(n2)
	if(is2digit(a)==0):
		continue
	else:
		n3=random.choice(copylist)
		b=n3
		copylist.remove(n3)
		z=a*b 
		if(is2digit(z)==0):
			continue
		else:
	#z digits should be unique and then need to be removed from the array copylist.
			if((z%10 in copylist) and (int(z/10)) in copylist):
				copylist.remove(z%10)
				copylist.remove(int(z/10))
			else:
				continue
			n4=random.choice(copylist)
			copylist.remove(n4)
			n5=random.choice(copylist)
			u=10*n4+n5
			copylist.remove(n5)
			if(is2digit(u)==0):
				continue
			else:
				v=u+z
				if(is2digit(v)==0):
					continue
				else:
					if((v%10 in copylist) and (int(v/10)) in copylist) and (v%10!=int(v/10)):
						copylist.remove(v%10)
						copylist.remove(int(v/10))
					else:
						continue
					if not copylist:#array copylist is empty. Then break and print the variables
						break
print(a)
print(b)
print(z)
print(u)
print(v)