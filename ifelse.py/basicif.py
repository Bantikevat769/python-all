# IF Statement simple
a = 2
b = 5

if a<b:
	print(a, 'is less than', b)

# cheak condition
a = 2

if a:
	print(a, 'is not zero')

# simple
a = 24
b = 5

if a<b:
	print(a, 'is less than', b)

#If with Multiple Conditions in the

a = 2
b = 5
c = 4

if a<b and a<c:
	print(a, 'is less than', b, 'and', c)

# Nested If simple to esay
a = 2

if a!=0:
	print(a, 'is not zero.')
	if a>0:
		print(a, 'is positive.')
	if a<0:
		print(a, 'is negative.')
#
#swaping program third varivle using
a=int(input("Enter any number"))
b=int(input("Enter any number"))
print("befor number A ",a)
print("befor number  B",b)
tem=a
a=b
b=tem
print("after number A ",a)
print("after number  B",b)